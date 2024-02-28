import machine
from machine import Pin, SoftI2C as I2C
import time
from mpu6050 import *
# MPU6050 registers and other constants
MPU_PWR_MGMT1_REG = 0x6B
MPU_ACCEL_XOUTH_REG = 0x3B
MPU_GYRO_XOUTH_REG = 0x43
MPU_ADDR = 0x68

class MPU6050:
    def __init__(self, sclpin, sdapin):
        self.i2c = I2C(scl=Pin(sclpin), sda=Pin(sdapin), freq=100000)
    
    def write_mpu6050_reg(self, reg, dat):
        self.i2c.writeto_mem(MPU_ADDR, reg, bytearray([dat]))
    
    def read_mpu6050_reg(self, reg):
        return self.i2c.readfrom_mem(MPU_ADDR, reg, 1)[0]
    
    def read_mpu6050_regs(self, reg, length):
        return self.i2c.readfrom_mem(MPU_ADDR, reg, length)
    
    def mpu_init(self):
        try:
            # Wake up MPU6050
            self.write_mpu6050_reg(MPU_PWR_MGMT1_REG, 0)
            return 0
        except OSError as e:
            print("Failed to initialize MPU6050:", e)
            return 1
    
    def get_acceleration(self):
        accel_raw = self.read_mpu6050_regs(MPU_ACCEL_XOUTH_REG, 6)
        accel = tuple(((accel_raw[i] << 8) | accel_raw[i+1]) for i in range(0, 6, 2))
        accel = tuple(map(lambda x: x if x < 32768 else x - 65536, accel))  # Convert to signed
        return accel
    
    def get_gyroscope(self):
        gyro_raw = self.read_mpu6050_regs(MPU_GYRO_XOUTH_REG, 6)
        gyro = tuple(((gyro_raw[i] << 8) | gyro_raw[i+1]) for i in range(0, 6, 2))
        gyro = tuple(map(lambda x: x if x < 32768 else x - 65536, gyro))  # Convert to signed
        return gyro

# Example usage
sclpin = 19
sdapin = 21
mpu = MPU6050(sclpin, sdapin)
if mpu.mpu_init() == 0:
    print("MPU6050 initialized successfully.")
    while True:
        accel = mpu.get_acceleration()
        gyro = mpu.get_gyroscope()
        print(f"Acceleration: {accel}, Gyroscope: {gyro}")
        time.sleep(1)
else:
    print("Error initializing MPU6050.")
