from machine import Pin, SoftI2C
import struct
import time

class MPU6050:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.address = 0x68  # Device I2C address
        self._accel_reg = 0x3B
        self._gyro_reg = 0x43
        self._power_mgmt_1 = 0x6B
        # Corrected from self._power_fear to self._power_mgmt_1
        self.i2c.writeto_mem(self.address, self._power_mgmt_1, b'\x00')  # Wake up the MPU6050
        time.sleep_ms(100)  # Ensure MPU6050 is powered up before proceeding

    def _read_data(self, reg, bytes=6):
        """Reads bytes from the given register."""
        data = self.i2c.readfrom_mem(self.address, reg, bytes)
        return struct.unpack(">hhh", data)

    def get_accel_data(self):
        """Returns accelerometer data."""
        ax, ay, az = self._read_data(self._accel_reg)
        # Convert from raw data to 'g' values
        # Assuming the accelerometer is set to ±2g range
        # 16,384 LSB/g (least significant bit per g)
        ax, ay, az = [a / 16384.0 for a in [ax, ay, az]]
        return ax, ay, az

    def get_gyro_data(self):
        """Returns gyroscope data."""
        gx, gy, gz = self._read_data(self._gyro_reg)
        # Convert from raw data to degrees per second
        # Assuming the gyroscope is set to ±250 degrees/s range
        # 131 LSB/(degrees/s)
        gx, gy, gz = [g / 131.0 for g in [gx, gy, gz]]
        return gx, gy, gz
