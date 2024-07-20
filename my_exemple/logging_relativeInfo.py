import logging
import sys
import time
from threading import Event
from cflib.crazyflie.log import LogConfig
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E1')

DEFAULT_HEIGHT = 0.1

deck_attached_event = Event()

logging.basicConfig(level=logging.ERROR)


def param_deck_flow(_, value_str):
    value = int(value_str)
    print(value)
    if value:
        deck_attached_event.set()
        print('Deck is attached!')
    else:
        print('Deck is NOT attached!')


def log_relative_pos_callback(timestamp, data, logconf):
    # print(str(data['rlInfo.tickInterval'])+':', end='')

    print('rlX1:', end='')
    print('%.3f' % data['rlInfo.X1'], end='')

    print(',rlY1:', end='')
    print('%.3f,' % data['rlInfo.Y1'], end='')

    print(',rlYaw1:', end='')
    print('%.3f,' % data['rlInfo.Yaw1'], end='')

    print(',rlX2:', end='')
    print('%.3f,' % data['rlInfo.X2'], end='')

    print(',rlY2:', end='')
    print('%.3f,' % data['rlInfo.Y2'])
    # print(',rlYaw2:'+str(data['rl_0_info.rlYaw2']))
    # print(data)
    pass


def add_relativeInfo_Log():
    logconf = LogConfig(name='rlInfo', period_in_ms=1000)
    # logconf.add_variable('rlInfo.tickInterval', 'uint32_t')
    logconf.add_variable('rlInfo.X1', 'float')
    logconf.add_variable('rlInfo.Y1', 'float')
    logconf.add_variable('rlInfo.Yaw1', 'float')
    logconf.add_variable('rlInfo.X2', 'float')
    logconf.add_variable('rlInfo.Y2', 'float')
    # logconf.add_variable('rlInfo.Yaw2', 'float')
    scf.cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_relative_pos_callback)
    logconf.start()
    time.sleep(1000)
    logconf.stop()


def param_setKeepflying(value):
    pass


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                         cb=param_deck_flow)
        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print('No flow deck detected!')
            sys.exit(1)
        add_relativeInfo_Log()
