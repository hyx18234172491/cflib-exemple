# https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_swarm_interface/

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



if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        swarm.parallel_safe(light_check)
