import os
import argparse
import cflib.crtp
from cflib.crtp.crtpstack import CRTPPacket
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

URI1 = 'radio://0/80/2M/1217E7E7E7'  #
URI2 = 'radio://0/80/2M/55E7E7E7E7'  #
URI3 = 'radio://0/80/2M/53E7E7E7E7'  #
URI4 = 'radio://0/80/2M/58E7E7E7E7'  #
URI5 = 'radio://0/80/2M/1147E7E7E7'  #
URI6 = 'radio://0/80/2M/57E7E7E7E7'
URI7 = 'radio://0/80/2M/54E7E7E7E7'  #
URI8 = 'radio://0/80/2M/31E7E7E7E7'  #
if __name__ == '__main__':
    os.system(f'cfloader reset-bootloader filename stm32-fw -w {URI6}')
    
