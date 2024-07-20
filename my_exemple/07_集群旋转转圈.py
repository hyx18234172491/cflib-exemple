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

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm

# Change uris and sequences according to your setup

URI1 = 'radio://0/80/2M/1217E7E7E7'
URI2 = 'radio://0/80/2M/55E7E7E7E7'
URI3 = 'radio://0/80/2M/53E7E7E7E7'
URI4 = 'radio://0/80/2M/58E7E7E7E7'
URI5 = 'radio://0/80/2M/1147E7E7E7'
URI6 = 'radio://0/80/2M/57E7E7E7E7'
URI7 = 'radio://0/80/2M/54E7E7E7E7'
URI8 = 'radio://0/80/2M/31E7E7E7E7'

z0 = 0.5
z = 1.0

x0 = 0.7
x1 = 0
x2 = -0.7

y0 = -1.0
y1 = -0.4
y2 = 0.4
y3 = 1.0

initDist = 1
high = 0.5
coordinates = [
    (0.0, -initDist, high),  # 1
    (-initDist, -initDist, high),  # 2
    (-initDist, 0.0, high),  # 3
    (-initDist, initDist, high),  # 4
    (0.0, initDist, high),  # 5
    (initDist, initDist, high),  # 6
    (initDist, 0.0, high),  # 7
    (initDist, -initDist, high),  # 8
]

sequences = []
for start in range(len(coordinates)):
    sequence = coordinates[start:] + coordinates[:start]
    sequences.append(sequence)

seq_args = {
    URI1: [sequences[0]],
    URI2: [sequences[1]],
    URI3: [sequences[2]],
    URI4: [sequences[3]],
    URI5: [sequences[4]],
    URI6: [sequences[5]],
    URI7: [sequences[6]],
    URI8: [sequences[7]],
}

# List of URIs, comment the one you do not want to fly
uris = {
    URI1,
    URI2,
    URI3,
    URI4,
    URI5,
    URI6,
    URI7,
    URI8,
}


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def take_off(cf):
    take_off_time = 1.0
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
            commander.go_to(position[0], position[1], position[2], 0, 3)
            time.sleep(3)
        land(cf, sequence[-1])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        # If the copters are started in their correct positions this is
        # probably not needed. The Kalman filter will have time to converge
        # any way since it takes a while to start them all up and connect. We
        # keep the code here to illustrate how to do it.
        # swarm.reset_estimators()

        # The current values of all parameters are downloaded as a part of the
        # connections sequence. Since we have 10 copters this is clogging up
        # communication and we have to wait for it to finish before we start
        # flying.
        print('Waiting for parameters to be downloaded...')
        swarm.parallel(wait_for_param_download)

        swarm.parallel(run_sequence, args_dict=seq_args)
