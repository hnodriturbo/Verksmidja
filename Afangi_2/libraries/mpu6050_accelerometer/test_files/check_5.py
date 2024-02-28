from machine import Pin, SoftI2C
import time
from mpu6050 import MPU6050  # Ensure this import matches the name of your MPU6050 library file

# Initialize I2C
scl_pin = 45  # Update to your SCL pin number
sda_pin = 21  # Update to your SDA pin number
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

# Initialize the MPU6050 sensor
mpu = MPU6050(sclpin=scl_pin, sdapin=sda_pin)

# Continuously read and print sensor data
while True:
    # Read accelerometer and gyroscope data
    accel_data = mpu.get_accel_data()
    gyro_data = mpu.get_gyro_data()

    # If your MPU6050 library supports temperature reading, you can include it
    temp = mpu.get_temp() if hasattr(mpu, 'get_temp') else 'N/A'

    # Print the sensor data
    print("Accelerometer data:", accel_data)
    print("Gyroscope data:", gyro_data)
    print("Temperature:", temp, "C")

    # Delay between readings
    time.sleep(1)
