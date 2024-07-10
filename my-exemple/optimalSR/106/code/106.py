"""
体现距离与测距周期之间的关系
"""

import logging
import utils

logging.basicConfig(level=logging.ERROR)

URI0 = 'radio://0/80/2M/55E7E7E7E7'

if __name__ == '__main__':
    # relative_pos
    log_var = {
        'recvSeq1': 'uint16_t',
        'recvNum1': 'uint16_t',
        'compute1num1': 'uint16_t',
        'compute2num1': 'uint16_t',

        'recvSeq2': 'uint16_t',
        'recvNum2': 'uint16_t',
        'compute1num2': 'uint16_t',
        'compute2num2': 'uint16_t',
    }

    utils.log_ranging(link_uri=URI0, log_cfg_name='Statistic', log_save_path='../data/test.csv',
                      log_var=log_var, period_in_ms=50, keep_time_in_s=100)

