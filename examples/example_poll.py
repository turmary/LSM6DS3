from lsm6ds3 import *
import time
import sys

# setup for IMU
imu = LSM6DS3(ACC_ODR=ACC_ODR_1_66_KHZ,
              GYRO_ODR=GYRO_ODR_1_66_KHZ,
              enable_acc=ENABLE_ACC_ALL_AXIS,
              enable_gyro=ENABLE_GYRO_ALL_AXIS,
              acc_scale=ACC_SCALE_16G,
              gyro_scale=GYRO_SCALE_2000DPS,
              acc_interrupt = False,
              gyro_interrupt = False)

def main():
    print("LSM6DS3 ID/WHO_AM_I = 0x%X" % imu.getID())
    while 1:
        try:
            time.sleep(0.3)
            # for raw data, imu.getAccData(raw=True)
            print('Accelerometer data [X, Y, Z]: %s' % imu.getAccData())
            # for raw data, imu.getGyroData(raw=True)
            print('Gyroscope data [X, Y, Z]: %s' % imu.getGyroData())
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print('Caught exception %s' % e)
            sys.exit(0)

if __name__ == '__main__':
    main()
