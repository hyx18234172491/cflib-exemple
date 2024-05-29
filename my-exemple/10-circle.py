import time
import math
from cflib.crazyflie import Crazyflie
import cflib.crtp
from cflib.positioning.motion_commander import MotionCommander
from threading import Thread

# Initialize the library
cflib.crtp.init_drivers()

# URIs of the two Crazyflie drones
URI_CENTER = 'radio://0/80/2M/34E7E7E7E7'
URI_ORBIT = 'radio://0/80/2M/50E7E7E7E7'

# Connect to the drones
cf_center = Crazyflie()
cf_orbit = Crazyflie()

# Helper function to make the center drone spin
def center_spin(cf):
    with MotionCommander(cf) as mc:
        while True:
            mc.start_turn_left(30)  # 30 degrees per second
            time.sleep(1)  # Adjust the sleep time as necessary

# Helper function to make the orbit drone fly in a circle around the center drone
def orbit_around_center(cf):
    with MotionCommander(cf) as mc:
        radius = 0.5
        speed = 0.2
        while True:
            for angle in range(0, 360, 5):
                radians = math.radians(angle)
                x = radius * math.cos(radians)
                y = radius * math.sin(radians)
                mc.move_distance(x, y, 0, velocity=speed)
                time.sleep(0.1)  # Adjust the sleep time as necessary

# Connect to both drones
cf_center.open_link(URI_CENTER)
cf_orbit.open_link(URI_ORBIT)

# Wait until connection is established
time.sleep(2)

# Start spinning the center drone and orbiting the second drone
thread_center = Thread(target=center_spin, args=(cf_center,))
thread_orbit = Thread(target=orbit_around_center, args=(cf_orbit,))

thread_center.start()
thread_orbit.start()

# Run for a specific duration
time.sleep(60)

# Stop the drones
cf_center.close_link()
cf_orbit.close_link()
