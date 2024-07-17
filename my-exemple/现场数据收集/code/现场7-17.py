import logging
import time
import threading
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
import datetime
from cflib.crazyflie.log import LogConfig
import pandas as pd
import xlsxwriter

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M/14E7E7E7E7'
lock = threading.Lock()
import pandas as pd
import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)
df = pd.DataFrame()
def log_stab_callback(timestamp, data, logconf):
    with lock:  # 使用锁锁住整个函数
        new_row_df = pd.DataFrame([data])
        print(data)
        # temp = {}
        # try:
        #     global mc
        #     mc.waitForNextFrame()
        #     for name, obj in mc.rigidBodies.items():
        #         temp[name + 'x'] = obj.position[0]
        #         temp[name + 'y'] = obj.position[1]
        #         temp[name + 'z'] = obj.position[2]
        # except:
        #     pass
        #
        # drone0_x, drone0_y, drone0_z = temp.get('UAV0x', 0), temp.get('UAV0y', 0), temp.get('UAV0z', 0)
        # drone1_x, drone1_y, drone1_z = temp.get('UAV1x', 0), temp.get('UAV1y', 0), temp.get('UAV1z', 0)
        # drone2_x, drone2_y, drone2_z = temp.get('UAV2x', 0), temp.get('UAV2y', 0), temp.get('UAV2z', 0)
        # drone3_x, drone3_y, drone3_z = temp.get('UAV3x', 0), temp.get('UAV3y', 0), temp.get('UAV3z', 0)
        #
        # distance_0_to_1 = calculate_distance(drone0_x, drone0_y, drone0_z, drone1_x, drone1_y, drone1_z)
        # #distance_2_to_1 = calculate_distance(drone2_x, drone2_y, drone2_z, drone1_x, drone1_y, drone1_z)
        # distance_3_to_1 = calculate_distance(drone3_x, drone3_y, drone3_z, drone1_x, drone1_y, drone1_z)
        #
        # new_row_df['distance_0_to_1'] = distance_0_to_1 * 100
        # #new_row_df['distance_2_to_1'] = distance_2_to_1 * 100
        # new_row_df['distance_3_to_1'] = distance_3_to_1 * 100

        # 将新数据添加到日志中或执行其他处理
        # 例如：logconf.add_row(new_row_df)
        global df
        df = pd.concat([df, new_row_df], ignore_index=True)

def simple_log_async(scf, logconf):

    cf = scf.cf
    # group = 'relative_ctrl'
    # name = 'relaCtrl_p'
    # full_name = group + "." + name
    # print("sucess")
    # #cf.param.set_value(full_name, 1)
    # print("flying")
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_stab_callback)

    logconf.start()
    time.sleep(200)
    logconf.stop()
    current_time = datetime.datetime.now()
    filename = current_time.strftime("optimal3_lighthouse%Y-%m-%d_%H-%M-%S") + ".xls"
    df.to_excel(filename)

def save_df_to_csv():
    global df
    current_time = datetime.datetime.now()
    filename = current_time.strftime("../data/optimal3_lighthouse_%Y-%m-%d_%H-%M-%S") + ".csv"
    df.to_csv(filename, index=False)
    print(f"DataFrame saved to {filename}")

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    # try:
    #     import motioncapture
    #
    #     mc = motioncapture.connect("vicon", {"hostname": "172.20.10.6"})
    #     print("connect sucess")
    # except:
    #     pass
    lg_stab = LogConfig(name='Statistic', period_in_ms=50)
    lg_stab.add_variable('Ranging.distTo0', 'int16_t')
    lg_stab.add_variable('Ranging.truthDistTo0', 'int16_t')
    lg_stab.add_variable('Ranging.distTo2', 'int16_t')
    lg_stab.add_variable('Ranging.truthDistTo2', 'int16_t')
    # lg_stab.add_variable('Ranging.distTo3', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo3', 'float')
    # lg_stab.add_variable('Ranging.distTo4', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo4', 'float')
    lg_stab.add_variable('Ranging.distTo5', 'int16_t')
    lg_stab.add_variable('Ranging.truthDistTo5', 'int16_t')
    # lg_stab.add_variable('Ranging.distTo6', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo6', 'float')
    # lg_stab.add_variable('Ranging.distTo7', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo7', 'float')
    # lg_stab.add_variable('Ranging.distTo8', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo8', 'float')
    # lg_stab.add_variable('Ranging.distTo9', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo9', 'float')
    # lg_stab.add_variable('Ranging.distTo1', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo3', 'float')
    # lg_stab.add_variable('Ranging.distTo0', 'float')
    # lg_stab.add_variable('Ranging.distTo0', 'float')
    #lg_stab.add_variable('Ranging.distTo1', 'float')
    #lg_stab.add_variable('Ranging.distTo2', 'float')
    # lg_stab.add_variable('Ranging.distTo3', 'float')
    # lg_stab.add_variable('Ranging.truthDistTo3', 'float')

    #lg_stab.add_variable('Ranging.distTo4', 'float')
    print("add_sucess")

    try:
        with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:

            simple_log_async(scf, lg_stab)
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        save_df_to_csv()