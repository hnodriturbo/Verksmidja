from machine import Pin, SoftI2C
import time

# Constants for the MPU6050
MPU6050_ADDR = 0x68
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
PWR_MGMT_1 = 0x6B
TEMP_OUT_H = 0x41

# Initialize I2C
scl_pin = 45  # Update to your SCL pin number
sda_pin = 21  # Update to your SDA pin number
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

def bytes_to_int(high_byte, low_byte, signed=True):
    value = (high_byte << 8) | low_byte
    if signed:
        value = value if value < 32768 else value - 65536
    return value

class MPU6050:
    def __init__(self, i2c, address=MPU6050_ADDR):
        self.i2c = i2c
        self.address = address
        # Wake up the MPU6050 as it starts in sleep mode
        self.i2c.writeto_mem(self.address, PWR_MGMT_1, b'\x00')

    def read_raw_data(self, reg, num_bytes):
        return self.i2c.readfrom_mem(self.address, reg, num_bytes)
        
    def get_accel_data(self):
        raw_data = self.read_raw_data(ACCEL_XOUT_H, 6)
        ax = bytes_to_int(raw_data[0], raw_data[1])
        ay = bytes_to_int(raw_data[2], raw_data[3])
        az = bytes_to_int(raw_data[4], raw_data[5])
        return (ax, ay, az)

    def get_gyro_data(self):
        raw_data = self.read_raw_data(GYRO_XOUT_H, 6)
        gx = bytes_to_int(raw_data[0], raw_data[1])
        gy = bytes_to_int(raw_data[2], raw_data[3])
        gz = bytes_to_int(raw_data[4], raw_data[5])
        return (gx, gy, gz)

    def get_temp(self):
        raw_data = self.read_raw_data(TEMP_OUT_H, 2)
        temp = bytes_to_int(raw_data[0], raw_data[1])
        # Convert the raw temperature to degrees Celsius
        return (temp / 340.0) + 36.53

mpu = MPU6050(i2c)

while True:
    accel_data = mpu.get_accel_data()
    gyro_data = mpu.get_gyro_data()
    temp = mpu.get_temp()
    
    print("\nAccelerometer data:", accel_data, "Gyroscope data:", gyro_data, "Temperature:", temp, "°C")
#     print("Gyroscope data:", gyro_data)
#     print("Temperature:", temp, "°C")
    
    time.sleep(1)
