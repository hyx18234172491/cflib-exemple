# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2017 Bitcraze AB
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
A script to fly 5 Crazyflies in formation. One stays in the center and the
other four fly around it in a circle. Mainly intended to be used with the
Flow deck.
The starting positions are vital and should be oriented like this

     

1    0    2

0号无人机为中心轴，1 2 号无人机绕着0号无人机旋转
     

The distance from the center to the perimeter of the circle is around 0.5 m

"""
import math
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm

# Change uris according to your setup
URI0 = 'radio://0/80/2M/E7E7E7E7E0'
URI1 = 'radio://0/80/2M/E7E7E7E7E1'
URI2 = 'radio://0/80/2M/E7E7E7E7E2'

# d: diameter of circle
# z: altitude 高度
params0 = {'d': 0, 'z': 0.5}
params1 = {'d': 1.0, 'z': 0.3}
params2 = {'d': 1.0, 'z': 0.3}


uris = {
    URI0,
    URI1,
    URI2,
}

params = {
    URI0: [params0],
    URI1: [params1],
    URI2: [params2],
}


def poshold(cf, t, z):  # t 秒飞到z高度
    steps = t * 10

    for r in range(steps):
        cf.commander.send_hover_setpoint(0, 0, 0, z)
        time.sleep(0.1)


def run_sequence(scf, params):
    cf = scf.cf

    # Number of setpoints sent per second
    fs = 4  # 每秒4次设置点
    fsi = 1.0 / fs  # 每次设置点的时间

    # Compensation for unknown error :-(
    comp = 1.3

    # Base altitude in meters
    base = 0.15  # 基础高度

    d = params['d']  # 圆直径
    z = params['z']  # 指定飞行高度

    poshold(cf, 2, base)  # 在2s内飞到base高度

    ramp = fs * 2   # 2s内从Base飞到指定高度z
    for r in range(ramp):
        cf.commander.send_hover_setpoint(0, 0, 0, base + r * (z - base) / ramp)  # vx, vy, yawrate, zdistance
        time.sleep(fsi)

    poshold(cf, 2, z)  # 2s内保持指定高度z

    for _ in range(2):
        # The time for one revolution
        circle_time = 8  # 一个循环8s

        steps = circle_time * fs  # 8s钟总共需要设置这么多次数
        for _ in range(steps):
            cf.commander.send_hover_setpoint(d * comp * math.pi / circle_time,
                                             0, 360.0 / circle_time, z)  # 周长/循环时间
            time.sleep(fsi)

    poshold(cf, 2, z)

    for r in range(ramp):
        cf.commander.send_hover_setpoint(0, 0, 0,
                                         base + (ramp - r) * (z - base) / ramp)
        time.sleep(fsi)

    poshold(cf, 1, base)

    cf.commander.send_stop_setpoint()


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        swarm.reset_estimators()
        swarm.parallel(run_sequence, args_dict=params)
