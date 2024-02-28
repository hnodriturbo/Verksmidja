from machine import Pin, SoftI2C
import time
# Adjust the import path according to your project structure
from mpu6050_files.my_mpu6050_class import MPU6050

# Setup I2C
scl_pin = 45  # SCL pin
sda_pin = 21  # SDA pin
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

# Initialize MPU6050
mpu = MPU6050(i2c)

while True:
    accel_data = mpu.read_accelerometer()
    gyro_data = mpu.read_gyroscope()
    print("Accelerometer:", accel_data)
    print("Gyroscope:", gyro_data)
    time.sleep(1)
