###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
########################################################### 
 
from machine import Pin, PWM, SoftI2C
import struct
import time

from car_components_files.settings_functions import initialize_pins

###########################################################
 ### ---- ----- My MPU6050  Class & Methods ----- ---- ###
###########################################################

class MPU6050:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.address = 0x68  # MPU6050 I2C address
        self._gyro_reg = 0x43
        self._power_mgmt_1 = 0x6B
        self.i2c.writeto_mem(self.address, self._power_mgmt_1, b'\x00')  # Wake up MPU6050
        time.sleep_ms(100)
        self.prev_time = time.ticks_ms()
        self.yaw = 0  # Initialize yaw at 0

    def _read_data(self, reg, bytes=6):
        data = self.i2c.readfrom_mem(self.address, reg, bytes)
        return struct.unpack(">hhh", data)

    def update_yaw(self):
        current_time = time.ticks_ms()
        elapsed_time = (current_time - self.prev_time) / 1000.0  # Convert ms to seconds
        _, _, gz = self.get_gyro_data()
        self.yaw += gz * elapsed_time  # Calculate change in yaw
        self.prev_time = current_time
        return self.yaw

    def get_gyro_data(self):
        gx, gy, gz = self._read_data(self._gyro_reg)
        # Gyroscope data conversion: degrees/s
        return gx / 131.0, gy / 131.0, gz / 131.0
    
    
    

    def calibrate_gyro(self, samples=100):
        print("Calibrating gyroscope...")
        z_bias = 0
        for _ in range(samples):
            _, _, z = self.get_gyro_data()
            z_bias += z
            time.sleep(0.01)
        z_bias /= samples
        print(f"Gyro Z-axis bias: {z_bias}")
        return z_bias


###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################
 

###########################################################
 #### ----- Ultrasonic Sensor Class And Methods ----- ####
###########################################################
        
class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin


    def measure_distance(self):
        # Trigger the measurement
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        
        # Wait for the echo to start
        while not self.echo.value():
            pass
        start = time.ticks_us()
        
        # Wait for the echo to end
        while self.echo.value():
            pass
        end = time.ticks_us()
        
        # Calculate the duration and distance
        duration = time.ticks_diff(end, start)
        distance = (duration * 0.0343) / 2  # Convert time to distance
        
        return distance


###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################
        
        
        
    # # # # # # ----- Storage ----- # # # # # #


# class MPU6050:
#     def __init__(self, scl_pin, sda_pin):
#         self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
#         self.address = 0x68  # Device I2C address
#         self._accel_reg = 0x3B
#         self._gyro_reg = 0x43
#         self._power_mgmt_1 = 0x6B
#         # Corrected from self._power_fear to self._power_mgmt_1
#         self.i2c.writeto_mem(self.address, self._power_mgmt_1, b'\x00')  # Wake up the MPU6050
#         time.sleep_ms(100)  # Ensure MPU6050 is powered up before proceeding
# 
#     def _read_data(self, reg, bytes=6):
#         """Reads bytes from the given register."""
#         data = self.i2c.readfrom_mem(self.address, reg, bytes)
#         return struct.unpack(">hhh", data)
# 
#     def get_accel_data(self):
#         """Returns accelerometer data."""
#         ax, ay, az = self._read_data(self._accel_reg)
#         # Convert from raw data to 'g' values
#         # Assuming the accelerometer is set to ±2g range
#         # 16,384 LSB/g (least significant bit per g)
#         ax, ay, az = [a / 16384.0 for a in [ax, ay, az]]
#         return ax, ay, az
# 
#     def get_gyro_data(self):
#         """Returns gyroscope data."""
#         gx, gy, gz = self._read_data(self._gyro_reg)
#         # Convert from raw data to degrees per second
#         # Assuming the gyroscope is set to ±250 degrees/s range
#         # 131 LSB/(degrees/s)
#         gx, gy, gz = [g / 131.0 for g in [gx, gy, gz]]
#         return gx, gy, gz

