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
import math
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm

# Change uris and sequences according to your setup

URI1 = 'radio://0/80/2M/50E7E7E7E7'  # 0号
URI2 = 'radio://0/80/2M/1207E7E7E7'  # 1号

high = 0.5


def solve_x2(y):
    if y < -1 or y > 1:
        raise ValueError("y值超出范围，必须满足 -1 <= y <= 1")

    x1 = 2 + math.sqrt(1 - y ** 2)
    x2 = 2 - math.sqrt(1 - y ** 2)

    return x2


def solve_x1(y):
    # 检查 y 是否在有效范围内
    if (y - 1) ** 2 > 1:
        raise ValueError("y 值超出范围，必须满足 (y-1)^2 <= 1")

    # 计算 x 的两个值
    x1 = 2 + math.sqrt(1 - (y - 1) ** 2)
    x2 = 2 - math.sqrt(1 - (y - 1) ** 2)

    return x1


def solve_x1_2(y):
    # 检查 y 是否在有效范围内
    if (y - 1) ** 2 > 1:
        raise ValueError("y 值超出范围，必须满足 (y-1)^2 <= 1")

    # 计算 x 的两个值
    x1 = 1 + math.sqrt(1 - (y - 1) ** 2)
    x2 = 1 - math.sqrt(1 - (y - 1) ** 2)

    return x1


def solve_x2_2(y):
    # 检查 y 是否在有效范围内
    if y < -1 or y > 1:
        raise ValueError("y 值超出范围，必须满足 -1 <= y <= 1")

    # 计算 x 的两个值
    x1 = 1 + math.sqrt(1 - y ** 2)
    x2 = 1 - math.sqrt(1 - y ** 2)

    return x2


fly_time = 1.5

sequences_0 = [
    (1, 0, high, 0, fly_time),

    (2, 0, high, 0, fly_time),  # 前进
    (2, 0, high, 3.14 / 8, fly_time),  # 旋转, 第3个参数是角度
    (2, 0, high, 3.14 / 4, fly_time),  # 旋转
    (2, 0, high, 3.14 / 3, fly_time),  # 旋转
    (2, 0, high, 3.14 / 2, fly_time),  # 旋转

    (2, 1, high, 3.14 / 2, fly_time),  # 前进
    (2, 1, high, 3.14 / 2 + 3.14 / 8, fly_time),  # 旋转
    (2, 1, high, 3.14 / 2 + 3.14 / 4, fly_time),  # 旋转
    (2, 1, high, 3.14 / 2 + 3.14 / 3, fly_time),  # 旋转
    (2, 1, high, 3.14 / 2 + 3.14 / 2, fly_time),  # 旋转

    (1, 1, high, 3.14 / 2 + 3.14 / 2, fly_time),  # 前进
    (1, 1, high, 3.14 + 3.14 / 8, fly_time),  # 旋转
    (1, 1, high, 3.14 + 3.14 / 4, fly_time),  # 旋转
    (1, 1, high, 3.14 + 3.14 / 3, fly_time),  # 旋转
    (1, 1, high, 3.14 + 3.14 / 2, fly_time),  # 旋转

    (1, 0, high, 3.14 + 3.14 / 2, fly_time),  # 前进
    (1, 0, high, 3.14 + 3.14 / 2 + 3.14 / 8, fly_time),  # 旋转
    (1, 0, high, 3.14 + 3.14 / 2 + 3.14 / 4, fly_time),  # 旋转
    (1, 0, high, 3.14 + 3.14 / 2 + 3.14 / 3, fly_time),  # 旋转
    (1, 0, high, 3.14 + 3.14 / 2 + 3.14 / 2, fly_time),  # 旋转

]

slow_time = 0.6
sequences_1 = [
    (0, 0, high, 0, fly_time),

    (0, 0, high, 0, slow_time),  # slow
    (1, 0, high, 0, fly_time - slow_time),  # 前进
    (solve_x2(0.25), -0.25, high, 0, fly_time),  # 旋转
    (solve_x2(0.50), -0.50, high, 0, fly_time),  # 旋转
    (solve_x2(0.75), -0.75, high, 0, fly_time),  # 旋转
    (solve_x2(1), -1, high, 0, fly_time),  # 旋转

    (solve_x2(1), -1, high, 0, slow_time),  # slow
    (2, 0, high, 0, fly_time - slow_time),  # 前进
    (solve_x1(0.25), 0.25, high, 0, fly_time),  # 旋转
    (solve_x1(0.50), 0.50, high, 0, fly_time),  # 旋转
    (solve_x1(0.75), 0.75, high, 0, fly_time),  # 旋转
    (solve_x1(1), 1, high, 0, fly_time),  # 旋转

    (solve_x1(1), 1, high, 0, slow_time),  # slow
    (2, 1, high, 0, fly_time - slow_time),  # 前进
    (solve_x1_2(1), 1, high, 0, fly_time),  # 旋转
    (solve_x1_2(1.25), 1.25, high, 0, fly_time),  # 旋转
    (solve_x1_2(1.5), 1.5, high, 0, fly_time),  # 旋转
    (solve_x1_2(2), 2, high, 0, fly_time),  # 旋转

    (solve_x1_2(2), 2, high, 0, slow_time),  # slow
    (1, 1, high, 0, fly_time - slow_time),  # 前进
    (solve_x2_2(1), 1, high, 0, fly_time),  # 旋转
    (solve_x2_2(0.75), 0.75, high, 0, fly_time),  # 旋转
    (solve_x2_2(0.5), 0.5, high, 0, fly_time),  # 旋转
    (solve_x2_2(0.25), 0.25, high, 0, fly_time),  # 旋转

]

seq_args = {
    URI1: [sequences_0],
    URI2: [sequences_1],
}

# List of URIs, comment the one you do not want to fly
uris = {
    URI1,
    URI2,
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
            commander.go_to(position[0], position[1], position[2], position[3], position[4])
            time.sleep(position[4])
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
