from machine import Pin, SoftI2C
import time

# Constants for MPU6050
MPU6050_ADDR = 0x68  # Device address
ACCEL_XOUT_H = 0x3B  # Accelerometer registers
GYRO_XOUT_H = 0x43   # Gyroscope registers
PWR_MGMT_1 = 0x6B    # Power management register

# Initialize I2C
scl_pin = 45  # Update to the correct pin if necessary
sda_pin = 21
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

class MPU6050:
    def __init__(self, i2c, address=MPU6050_ADDR):
        self.i2c = i2c
        self.address = address
        self.i2c.writeto_mem(self.address, PWR_MGMT_1, b'\x00')  # Wake up the MPU6050
    
    def read_raw_values(self, reg):
        # Reads 14 bytes from the specified register
        data = self.i2c.readfrom_mem(self.address, reg, 14)
        return data
    
    def get_accel_data(self):
        # Reads the raw accelerometer data
        raw_data = self.read_raw_values(ACCEL_XOUT_H)
        ax = int.from_bytes(raw_data[0:2], 'big', signed=True)
        ay = int.from_bytes(raw_data[2:4], 'big', signed=True)
        az = int.from_bytes(raw_data[4:6], 'big', signed=True)
        return (ax, ay, az)
    
    def get_gyro_data(self):
        # Reads the raw gyroscope data
        raw_data = self.read_raw_values(GYRO_XOUT_H)
        gx = int.from_bytes(raw_data[8:10], 'big', signed=True)
        gy = int.from_bytes(raw_data[10:12], 'big', signed=True)
        gz = int.from_bytes(raw_data[12:14], 'big', signed=True)
        return (gx, gy, gz)

    def get_temp(self):
        # Reads the temperature
        raw_data = self.read_raw_values(ACCEL_XOUT_H)
        temp_raw = int.from_bytes(raw_data[6:8], 'big', signed=True)
        # Formula to convert the raw temperature to degrees Celsius
        temp = (temp_raw / 340.0) + 36.53
        return temp

mpu = MPU6050(i2c)

while True:
    accel_data = mpu.get_accel_data()
    gyro_data = mpu.get_gyro_data()
    temp = mpu.get_temp()
    
    print("Accelerometer data:", accel_data)
    print("Gyroscope data:", gyro_data)
    print("Temperature:", temp, "C")
    
    time.sleep(1)
