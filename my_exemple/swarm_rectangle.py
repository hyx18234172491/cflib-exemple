# https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_swarm_interface/
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie import syncCrazyflie
from cflib.crazyflie.log import LogConfig

SWARM_NUM = 3
logconf = []


def activate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 255)


def deactivate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 0)


def light_check(scf):
    activate_led_bit_mask(scf)
    time.sleep(4)
    deactivate_led_bit_mask(scf)
    time.sleep(2)


uris = [
    'radio://0/80/2M/E7E7E7E7E1',
    'radio://0/80/2M/E7E7E7E7E2',
    'radio://0/80/2M/E7E7E7E7E3',
    # 'radio://0/20/2M/E7E7E7E704',
    # Add more URIs if you want more copters in the swarm
]

# The layout of the positions (1m apart from each other):
#   <------ 1 m ----->
#   0                1
#          ^              ^
#          |Y             |
#          |              |
#          +------> X    1 m
#                         |
#                         |
#   3               2     .


h = 0  # remain constant height similar to take off height
x0, y0 = +0.3, +0.3
x1, y1 = -0.3, -0.3

#    x   y   z  time
sequence0 = [
    (x1, y0, h, 3.0),
    (x0, y1, h, 3.0),
    (x0,  0, h, 3.0),
]

sequence1 = [
    (x0, y0, h, 3.0),
    (x1, y1, h, 3.0),
    (.0, y1, h, 3.0),
]

sequence2 = [
    (x0, y1, h, 3.0),
    (x1, y0, h, 3.0),
    (x1,  0, h, 3.0),
]

sequence3 = [
    (x1, y1, h, 3.0),
    (x0, y0, h, 3.0),
    (.0, y0, h, 3.0),
]

seq_args = {
    uris[0]: [sequence0],
    uris[1]: [sequence1],
    uris[2]: [sequence2],
    # uris[3]: [sequence3],
}


def run_sequence(scf: syncCrazyflie.SyncCrazyflie, sequence):
    cf = scf.cf

    for arguments in sequence:
        commander = scf.cf.high_level_commander

        x, y, z = arguments[0], arguments[1], arguments[2]
        duration = arguments[3]

        print('Setting position {} to cf {}'.format((x, y, z), cf.link_uri))
        commander.go_to(x, y, z, 0, duration, relative=True)
        time.sleep(duration)


def log_pos_callback(timestamp, data, logconf):
    print(data)
    global position_estimate
    position_estimate[0] = data['stateEstimate.x']
    position_estimate[1] = data['stateEstimate.y']


def run_add_same_log(scf):
    # 添加日志

    for i in SWARM_NUM:
        global logconf
        logconf[i] = LogConfig(name='Position', period_in_ms=10)
        logconf[i].add_variable('stateEstimate.x', 'float')
        logconf[i].add_variable('stateEstimate.y', 'float')
        scf.cf.log.add_config(logconf[i])
        logconf[i].data_received_cb.add_callback(log_pos_callback)


def run_add_same_log_start(scf):
    for i in SWARM_NUM:
        logconf[i].start()


def run_add_same_log_stop(scf):
    for i in SWARM_NUM:
        logconf[i].stop()


def take_off(scf):
    duration = 3
    commander = scf.cf.high_level_commander
    # absolute_height_m,duration_s(持续秒数)
    commander.takeoff(0.3, duration)
    time.sleep(duration)


def land(scf):
    commander = scf.cf.high_level_commander

    commander.land(0.0, 3.0)
    time.sleep(3)

    commander.stop()


if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        # swarm.parallel_safe(light_check)

        swarm.reset_estimators()

        swarm.parallel_safe(take_off)
        # # swarm.parallel_safe(run_square_sequence)
        # # 添加日志
        # swarm.parallel_safe(run_add_same_log)
        # # 启动日志
        # swarm.parallel_safe(run_add_same_log_start)

        swarm.parallel_safe(run_sequence, args_dict=seq_args)
        swarm.parallel_safe(land)
        # # 关闭日志
        # swarm.parallel_safe(run_add_same_log_stop)
