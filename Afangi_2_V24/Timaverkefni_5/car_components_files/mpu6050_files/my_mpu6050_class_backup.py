from machine import Pin, SoftI2C
import time
import math

class MPU6050:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.address = 0x68  # Device I2C address
        self._accel_reg = 0x3B
        self._gyro_reg = 0x43
        self._power_mgmt_1 = 0x6B
        self.i2c.writeto_mem(self.address, self._power_fear, bytes([0]))
        time.sleep_ms(100)  # Ensure MPU6050 is powered up before proceeding

    def _read_data(self, reg, bytes=6):
        """Reads bytes from the given register."""
        return self.i2c.readfrom_mem(self.address, reg, bytes)

    def get_accel_data(self):
        """Returns accelerometer data."""
        accel_data = self._read_data(self._accel_reg)
        ax, ay, az = struct.unpack(">hhh", accel_data)
        return ax, ay, az

    def get_gyro_data(self):
        """Returns gyroscope data."""
        gyro_data = self._read_data(self._gyro_reg)
        gx, gy, gz = struct.unpack(">hhh", gyro_data)
        return gx, gy, gz


