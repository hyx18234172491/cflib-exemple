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


def run_square_sequence(scf):
    # 飞一个正方形区域
    box_size = 1
    flight_time = 2

    commander = scf.cf.high_level_commander

    commander.go_to(box_size, 0, 0, 0, flight_time, relative=True)
    time.sleep(flight_time)

    commander.go_to(0, box_size, 0, 0, flight_time, relative=True)
    time.sleep(flight_time)

    commander.go_to(-box_size, 0, 0, 0, flight_time, relative=True)
    time.sleep(flight_time)

    commander.go_to(0, -box_size, 0, 0, flight_time, relative=True)
    time.sleep(flight_time)


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


def hover_sequence(scf):
    take_off(scf)
    land(scf)


if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        # swarm.parallel_safe(light_check)

        swarm.reset_estimators()

        swarm.parallel_safe(take_off)
        # swarm.parallel_safe(hover_sequence)
        swarm.parallel_safe(run_square_sequence)
        # # 添加日志
        # swarm.parallel_safe(run_add_same_log)
        # # 启动日志
        # swarm.parallel_safe(run_add_same_log_start)

        swarm.parallel_safe(land)
        # # 关闭日志
        # swarm.parallel_safe(run_add_same_log_stop)
