from machine import Pin, SoftI2C as I2C
from mpu6050 import MPU6050  # Adjust import path as necessary
import time
# Initialize I2C
scl_pin = 45  # Adjust to your SCL pin
sda_pin = 21  # Adjust to your SDA pin
i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

# Initialize MPU6050
mpu = MPU6050(sclpin=scl_pin, sdapin=sda_pin)

if mpu.MPU_Init() == 0:
    print("MPU6050 initialization successful.")
else:
    print("Failed to initialize MPU6050.")

# Continuously read from MPU6050
while True:
    accel = mpu.MPU_Get_Accelerometer()
    gyro = mpu.MPU_Get_Gyroscope()
    print("Accel:", accel, "Gyro:", gyro)
    time.sleep(1)
