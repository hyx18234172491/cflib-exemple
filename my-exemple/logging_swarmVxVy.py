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

URI = uri_helper.uri_from_env(default='radio://0/80/2M/53E7E7E7E7')

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
    print(data)


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                         cb=param_deck_flow)
        time.sleep(1)

        logconf = LogConfig(name='swarmstate', period_in_ms=10)
        logconf.add_variable('swarmstate.swaVx', 'float')
        logconf.add_variable('swarmstate.swaVy', 'float')
        logconf.add_variable('swarmstate.swaGz', 'float')
        logconf.add_variable('swarmstate.swah', 'float')
        scf.cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_relative_pos_callback)

        if not deck_attached_event.wait(timeout=5):
            print('No flow deck detected!')
            sys.exit(1)

        logconf.start()
        time.sleep(1000)
        logconf.stop()
