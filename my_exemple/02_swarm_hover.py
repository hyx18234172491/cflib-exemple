# https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_swarm_interface/
'''
初始摆放位置为一个三角形，机头方向为正三角形的三个角的方向

执行代码后，先是三角形变大，后变小，再变大，再变小

'''
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie import syncCrazyflie
from cflib.crazyflie.log import LogConfig


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
    'radio://0/80/2M/1217E7E7E7',
    'radio://0/80/2M/53E7E7E7E7',
    # 'radio://0/80/2M/64E7E7E7E7',
    'radio://0/80/2M/55E7E7E7E7',
    'radio://0/80/2M/58E7E7E7E7',
    'radio://0/80/2M/1147E7E7E7',
    'radio://0/80/2M/57E7E7E7E7'
     # 'radio://0/80/2M/E7E7E7E7E3',
     # 'radio://0/20/2M/E7E7E7E704',
     # Add more URIs if you want more copters in the swarm
]

# uris = [
#     'radio://0/80/2M/55E7E7E7E7',
#     # 'radio://0/80/2M/E7E7E7E7E3',
#     # 'radio://0/20/2M/E7E7E7E704',
#     # Add more URIs if you want more copters in the swarm
# ]



def take_off(scf):
    duration = 300
    commander = scf.cf.high_level_commander
    # absolute_height_m,duration_s(持续秒数)
    commander.takeoff(0.4, 1)
    time.sleep(duration+1)


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

        # swarm.reset_estimators()
        print("ready to fly")
        swarm.parallel_safe(hover_sequence)
        # swarm.parallel_safe(hover_sequence)
        # swarm.parallel_safe(land)
