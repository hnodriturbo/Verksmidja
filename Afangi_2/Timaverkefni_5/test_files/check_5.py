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






# Basic imports
from machine import Pin, SoftI2C
import time


# Import the class for testing
from car_components_files.addons import MPU6050




# Setup I2C
scl_pin = 45  # SCL pin
sda_pin = 21  # SDA pin
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))




# Scan for devices and print the address or the device
devices = i2c.scan()
print("I2C devices found:", devices)


mpu = MPU6050(scl_pin=45, sda_pin=21)  # Modify the GPIOs as required in your context




# Reading the sensor for only Yaw is one angle, assuming your car's flat and moving only on the z-axis.
# A general utilization might rely on a PID to handle sensor's report to re-steer your car.
while True:
    ax, ay, az = mpu.get_accel_data()
    # Note: ax, ay, and az return as proportional rates to g (9.81 m/s²).
    # e.g., checking for movement along the car's intended right
    print(f"Acceleration X: {ax}, Y: {ay}, Z: {az}")
    time.sleep(1)
