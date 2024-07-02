# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2017-2018 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
Version of the AutonomousSequence.py example connecting to 10 Crazyflies.
The Crazyflies go straight up, hover a while and land but the code is fairly
generic and each Crazyflie has its own sequence of setpoints that it files
to.

The layout of the positions:
    x2      x1      x0

y3  10              4

            ^ Y
            |
y2  9       6       3
            |
            +------> X

y1  8       5       2



y0  7               1

"""
import time

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

URI1 = 'radio://0/80/2M/31E7E7E7E7'  # uwb1
URI2 = 'radio://0/80/2M/55E7E7E7E7'  # uwb2
# URI3 = 'radio://0/80/2M/53E7E7E7E7'  #
# URI4 = 'radio://0/80/2M/58E7E7E7E7'  #
# URI5 = 'radio://0/80/2M/1147E7E7E7'  #
# URI6 = 'radio://0/80/2M/57E7E7E7E7'
# URI7 = 'radio://0/80/2M/54E7E7E7E7'  #
# URI8 = 'radio://0/80/2M/31E7E7E7E7'  #
# URI9 = 'radio://0/80/2M/43E7E7E7E7'  #



high = 0.5

sequences = [
    # 组号，x，y，z, yaw, duration
]
flight_duration = 20
sequences.append([0, 0, 0, high, 0, flight_duration])

list1 = [
    [1, 1, 0, 0, 0, flight_duration/10],
    [1, -1, 0, 0, 0, flight_duration/10],
    [1, 1, 0, 0, 0, flight_duration/10],
    [1, -1, 0, 0, 0, flight_duration/10],
    [1, 1, 0, 0, 0, flight_duration/10],
    [1, -1, 0, 0, 0, flight_duration/10],
    [1, 1, 0, 0, 0, flight_duration/10],
    [1, -1, 0, 0, 0, flight_duration/10],
    [1, 1, 0, 0, 0, flight_duration/10],
    [1, -1, 0, 0, 0, flight_duration/10]

]
sequences.append(list1)
# for i in range(0,)

seq_args = {
    URI1: [sequences[0]],
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
    URI1,
    URI2,
    # URI3,
    # URI4,
    # URI5,
    # URI6,
    # URI7,
    # URI8,
    # # URI9,
}


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def take_off(cf):
    take_off_time = 1
    print(f'takeoff high:{high}')
    commander = cf.high_level_commander
    commander.takeoff(high, take_off_time)
    time.sleep(take_off_time)


def land(cf, position):
    landing_time = 1.0
    sleep_time = 0.1
    steps = int(landing_time / sleep_time)
    vz = -position[2] / landing_time

    print(vz)

    for _ in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)

    cf.commander.send_stop_setpoint()
    # Make sure that the last packet leaves before the link is closed
    # since the message queue is not flushed before closing
    time.sleep(0.1)


def run_sequence(scf, sequence):
    try:
        cf = scf.cf

        take_off(cf)
        commander = cf.high_level_commander
        for position in sequence:
            print('Setting position {}'.format(position))
            # x ,y ,z, 不知道, time
            commander.go_to(x=position[1], y=position[2], z=position[3], yaw=0, duration_s=3, relative=True)
            time.sleep(3)
        land(cf, sequence[-1])
    except Exception as e:
        print(e)


def logCallback(timestamp, data, logconf):
    global log_var,log_data
    temp = {}
    temp['timestamp'] = timestamp
    temp['logNumber'] = logconf.name
    print(logconf.name)
    for log_var_name, log_var_type in log_var.items():
        temp[log_var_name] = data[log_var_name]
    # try:
    #     global mc
    #     for name, obj in mc.rigidBodies.items():
    #
    #         print(name, obj.position, obj.rotation.z)
    #         temp[name+'x'] = obj.position[0]
    #         temp[name + 'y'] = obj.position[1]
    #         temp[name + 'z'] = obj.position[2]
    # except:
    #     pass

    log_data = log_data.append(temp, ignore_index=True)
    pass


def addLogConfig(scf, sequence):
    logconf = LogConfig(name='log'+str(sequence[0]), period_in_ms=50)
    global log_var
    for log_var_name, log_var_type in log_var.items():
        logconf.add_variable(log_var_name, log_var_type)
    scf.cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(logCallback)
    logconf.start()


if __name__ == '__main__':
    log_var = {
        'Statistic.recvSeq1': 'uint16_t',
        'Statistic.recvNum1': 'uint16_t',
        'Statistic.compute1num1': 'uint16_t',
        'Statistic.compute2num1': 'uint16_t',
        'Statistic.dist1': 'int16_t',
        'Statistic.distSrc1': 'uint8_t',

        'Statistic.recvSeq2': 'uint16_t',
        'Statistic.recvNum2': 'uint16_t',
        'Statistic.compute1num2': 'uint16_t',
        'Statistic.compute2num2': 'uint16_t',
        'Statistic.dist2': 'int16_t',
        'Statistic.distSrc2': 'uint8_t',
    }
    # log_data = pd.DataFrame(columns=['logNumber',log_var.keys()])
    log_data = pd.DataFrame()
    # try:
    #     import motioncapture
    #     mc = motioncapture.connect("vicon", {"hostname": "192.168.229.10"})
    # except:
    #     pass
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        # The current values of all parameters are downloaded as a part of the
        # connections sequence. Since we have 10 copters this is clogging up
        # communication and we have to wait for it to finish before we start
        # flying.
        print('Waiting for parameters to be downloaded...')
        swarm.parallel(wait_for_param_download)

        swarm.parallel(addLogConfig, args_dict=seq_args)
        # swarm.parallel(run_sequence, args_dict=seq_args)
        time.sleep(20)
    log_data.to_csv('test.csv')