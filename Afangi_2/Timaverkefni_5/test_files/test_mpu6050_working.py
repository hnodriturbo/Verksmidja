###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
########################################################### 



from machine import Pin, SoftI2C
import time

# Adjusted import path to match the new folder structure
from car_components_files.addons import MPU6050

# Setup I2C
scl_pin = 45  # SCL pin
sda_pin = 21  # SDA pin
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

# Scan for devices and print the address or the device
devices = i2c.scan()
print("I2C devices found:", devices)

# Initialize MPU6050 - Create the instance
mpu = MPU6050(i2c)

while True:
    accel_data = mpu.get_accel_data()
    # gyro_data = mpu.get_gyro_data()
    print("Accelerometer:", accel_data)
    # print("Gyroscope:", gyro_data)
    time.sleep(1)
