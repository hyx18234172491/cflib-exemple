import time
import warnings

warnings.filterwarnings("ignore")

import pandas as pd

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
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

# Change uris and sequences according to your setup
URI0 = 'radio://0/80/2M/53E7E7E7E7'  # uwb0
URI1 = 'radio://0/80/2M/14E7E7E7E7'  # uwb1
URI2 = 'radio://0/80/2M/68E7E7E7E7'  # uwb2
URI3 = 'radio://0/80/2M/1297E7E7E7'  # uwb3
URI4 = 'radio://0/80/2M/31E7E7E7E7'  # uwb4
URI5 = 'radio://0/80/2M/33E7E7E7E7'  # uwb5
URI6 = 'radio://0/80/2M/72E7E7E7E7'  # uwb6
URI7 = 'radio://0/80/2M/56E7E7E7E7'  #
URI8 = 'radio://0/80/2M/31E7E7E7E7'  #
URI9 = 'radio://0/80/2M/90E7E7E7E7'  #
URI10 = 'radio://0/80/2M/76E7E7E7E7'  #
URI11 = 'radio://0/80/2M/28E7E7E7E7'  #
URI12 = 'radio://0/80/2M/86E7E7E7E7'  #
URI13 = 'radio://0/80/2M/42E7E7E7E7'  #
URI14 = 'radio://0/80/2M/42E7E7E7E7'  #
URI15 = 'radio://0/80/2M/50E7E7E7E7'  #
URI16 = 'radio://0/80/2M/16E7E7E7E7'  #

URI17 = 'radio://0/80/2M/9E7E7E7E7'  #
URI18 = 'radio://0/80/2M/21E7E7E7E7'  #


sequences = []

sequences.append([['0']])
sequences.append([['1']])

seq_args = {
    URI0: [sequences[0]],
    URI2: [sequences[1]],
    # URI3: [sequences[2]],
    # URI4: [sequences[3]],
    # URI5: [sequences[4]],
    # URI6: [sequences[5]],
    # URI7: [sequences[6]],
    # URI8: [sequences[7]],
    # URI9: [sequences[8]],
}

# List of URIs, comment the one you do not want to fly
uris = {
    URI0,
    # URI1,
    URI2,
    # URI3,
    # URI4,
    # URI5,
    # URI6,
    # URI7,
    # URI8,
    # # URI9,
    # URI13
}


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def logCallback(timestamp, data, logconf):
    global log_var, log_data
    temp = {}
    temp['timestamp'] = timestamp
    temp['logNumber'] = logconf.name
    print(logconf.name)
    for log_var_name, log_var_type in log_var.items():
        temp[log_var_name] = data[log_var_name]

    log_data = log_data.append(temp, ignore_index=True)
    pass


def addLogConfig(scf, sequence):
    print(sequence[0][0])
    logconf = LogConfig(name='log' + str(sequence[0][0]), period_in_ms=30)

    global log_var
    for log_var_name, log_var_type in log_var.items():
        logconf.add_variable(log_var_name, log_var_type)
    scf.cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(logCallback)
    logconf.start()


if __name__ == '__main__':
    log_var = {
        'Statistic.recvSeq2': 'uint16_t',
        'Statistic.recvNum2': 'uint16_t',
        'Statistic.compute1num2': 'uint16_t',
        'Statistic.compute2num2': 'uint16_t',

        'Statistic.recvSeq0': 'uint16_t',
        'Statistic.recvNum0': 'uint16_t',
        'Statistic.compute1num0': 'uint16_t',
        'Statistic.compute2num0': 'uint16_t',
    }
    log_data = pd.DataFrame()
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Waiting for parameters to be downloaded...')
        swarm.parallel(wait_for_param_download)

        swarm.parallel(addLogConfig, args_dict=seq_args)
        time.sleep(100)
    log_data.to_csv('../data/test.csv')
