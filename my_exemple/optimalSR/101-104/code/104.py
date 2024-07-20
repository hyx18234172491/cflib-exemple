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
        'recvSeq': 'uint16_t',
        'recvNum': 'uint16_t',
        'compute1num': 'uint16_t',
        'compute2num': 'uint16_t',
    }

    utils.log_ranging(link_uri=URI0, log_cfg_name='Statistic', log_save_path='../../106/data/24架最佳性能-60+rand(40).csv',
                      log_var=log_var, period_in_ms=50, keep_time_in_s=100)

