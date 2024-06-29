"""
体现距离与测距周期之间的关系
"""

import cflib.crtp
import numpy as np
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
import time
import logging
import pandas as pd
from multiprocessing import Process
import utils

logging.basicConfig(level=logging.ERROR)

URI0 = 'radio://0/80/2M/55E7E7E7E7'

if __name__ == '__main__':
    # relative_pos
    log_var = {
        'recvSeq': 'uint16_t',
        'recvNum': 'uint16_t',
        'compute1num': 'uint16_t',
        'compute2num': 'uint16_t',
    }

    utils.log_ranging(link_uri=URI0, log_cfg_name='Statistic', log_save_path='../data/102-3-50ms-30loss-100s-1.csv',
                      log_var=log_var, period_in_ms=50, keep_time_in_s=100)

