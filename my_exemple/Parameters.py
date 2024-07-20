import logging
import sys
import time

from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

# loging packet
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncLogger import SyncLogger

from threading import Event
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


def param_stab_est_callback(name, value):
    print('The crazyflie has parameter ' + name + ' set at number: ' + value)


def simple_param_async(scf, groupstr, namestr):
    cf = scf.cf
    full_name = groupstr + "." + namestr
    cf.param.add_update_callback(group=groupstr, name=namestr,
                                 cb=param_stab_est_callback)
    time.sleep(1)
    cf.param.set_value(full_name, 2)
    time.sleep(1)
    cf.param.set_value(full_name, 1)
    time.sleep(1)


if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    # Add logging config
    lg_stab = LogConfig(name='Stabilizer', period_in_ms=10)
    lg_stab.add_variable('stabilizer.roll', 'float')
    lg_stab.add_variable('stabilizer.pitch', 'float')
    lg_stab.add_variable('stabilizer.yaw', 'float')

    # -----------------------------------#
    group = "stabilizer"
    name = "estimator"
    # -----------------------------------#
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:

        # 执行
        simple_param_async(scf, group, name)
