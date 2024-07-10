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

# URI = uri_helper.uri_from_env(default='radio://0/80/2M/50E7E7E7E7')
URI = uri_helper.uri_from_env(default='radio://0/80/2M/26E7E7E7E7')

DEFAULT_HEIGHT = 0.3
BOX_LIMIT = 0.5


def take_off(scf):
    duration = 1
    commander = scf.cf.high_level_commander
    # absolute_height_m,duration_s(持续秒数)
    commander.takeoff(0.4, duration)
    time.sleep(duration)


import keyboard
import time
import random

x_vel = 0
y_vel = 0


def on_up_arrow():
    print("向上键被按下")
    global x_vel, y_vel
    x_vel =  0.05
    y_vel = 0

def on_down_arrow():
    print("向下键被按下")
    global x_vel, y_vel
    x_vel = -0.05
    y_vel = 0


def on_left_arrow():
    print("向 左键被按下")
    global x_vel, y_vel
    x_vel = 0
    y_vel = 0.05


def on_right_arrow():
    print("向右键被按下")
    global x_vel, y_vel
    x_vel = 0
    y_vel = -0.05


def on_space():
    print("空格键被按下")
    global x_vel, y_vel
    x_vel = 0
    y_vel = 0


def no_key_pressed():
    print("无按键被按下")
    # global x_vel, y_vel
    # x_vel = 0
    # y_vel = 0


# 注册热键
keyboard.on_press_key("up", lambda _: on_up_arrow())
keyboard.on_press_key("left", lambda _: on_left_arrow())
keyboard.on_press_key("right", lambda _: on_right_arrow())
keyboard.on_press_key("down", lambda _: on_down_arrow())
keyboard.on_press_key("space", lambda _: on_space())

if __name__ == '__main__':

    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
            take_off(scf)  # 先takeoff
            try:
                while True:
                    if not keyboard.is_pressed("up") and not keyboard.is_pressed("left") and not keyboard.is_pressed(
                            "space") and not keyboard.is_pressed("right") and not keyboard.is_pressed("down"):
                        no_key_pressed()

                        mc.start_linear_motion(x_vel, y_vel, 0)
                        time.sleep(0.1)  # 延迟以减少CPU使用率
            except KeyboardInterrupt:
                   print("程序已终止")
