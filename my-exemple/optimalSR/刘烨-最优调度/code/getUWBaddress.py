import logging
import sys
import time

from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from cflib.crazyflie.syncLogger import SyncLogger
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
import cflib.crtp


def setJitterParamter(scf):
    global jitter
    cf = scf.cf
    cf.param.set_value('Statistic.jitter', jitter)
    time.sleep(0.1)


def printUWB_ADDRESS(scf):
    cf = scf.cf
    UWB_ADDRESS = cf.param.get_value('ADHOC.MY_UWB_ADDRESS')
    print(UWB_ADDRESS)


uris = [
    'radio://0/80/2M/26E7E7E7E7',  # uwb0
    'radio://0/80/2M/14E7E7E7E7',  # uwb1
    'radio://0/80/2M/68E7E7E7E7',  # uwb2
    'radio://0/80/2M/1297E7E7E7',  # uwb3
    'radio://0/80/2M/31E7E7E7E7',  # uwb4
    'radio://0/80/2M/33E7E7E7E7',  # uwb5
    'radio://0/80/2M/72E7E7E7E7',  # uwb6
    'radio://0/80/2M/56E7E7E7E7',  # uwb7
    'radio://0/80/2M/31E7E7E7E7',  # uwb8
    'radio://0/80/2M/90E7E7E7E7',  # uwb9
    'radio://0/80/2M/76E7E7E7E7',  # uwb10
    'radio://0/80/2M/28E7E7E7E7',  # uwb11
    'radio://0/80/2M/86E7E7E7E7',  # uwb12
    'radio://0/80/2M/42E7E7E7E7',  # uwb13
    'radio://0/80/2M/35E7E7E7E7',  # uwb14
    'radio://0/80/2M/50E7E7E7E7',  # uwb15
    'radio://0/80/2M/16E7E7E7E7',  # uwb16
    'radio://0/80/2M/9E7E7E7E7',  # uwb17
    'radio://0/80/2M/21E7E7E7E7'  # uwb18
    'radio://0/80/2M/22E7E7E7E7'  # uwb19
    'radio://0/80/2M/23E7E7E7E7'  # uwb20
    'radio://0/80/2M/27E7E7E7E7'  # uwb21
    'radio://0/80/2M/1267E7E7E7'  # uwb22

    'radio://0/80/2M/17E7E7E7E7'  # uwb24
    'radio://0/80/2M/57E7E7E7E7'  # uwb25

    'radio://0/80/2M/53E7E7E7E7'  # uwb26
    'radio://0/80/2M/18E7E7E7E7'  # uwb27

]
start = 11
uris = uris[start:start + 1]
if __name__ == '__main__':
    # Initialize the low-level drivers
    try:
        # Initialize the low-level drivers
        cflib.crtp.init_drivers()
        factory = CachedCfFactory(rw_cache='./cache')
        with Swarm(uris, factory=factory) as swarm:
            swarm.parallel_safe(printUWB_ADDRESS)
            print('打印完毕')
    except Exception as e:
        print(f"An error occurred: {e}")
