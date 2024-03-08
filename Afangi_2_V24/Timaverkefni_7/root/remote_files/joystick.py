# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## ----------------- Created March '24 ----------------- ##
# ###########################################################



from machine import Pin, ADC, SoftI2C
import time
from lib.i2c_lcd import I2cLcd




class Joystick:
    def __init__(self, VRx_pin, VRy_pin, button_pin):
        self.VRx = ADC(Pin(VRx_pin), atten=ADC.ATTN_11DB)
        self.VRy = ADC(Pin(VRy_pin), atten=ADC.ATTN_11DB)
        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
        self.calibrate()

    def calibrate(self):
        print("Calibrating joystick... Center the joystick now.")
        time.sleep(2)  # Give time to center the joystick
        self.center_x = self.VRx.read()
        self.center_y = self.VRy.read()
        print(f"Calibration complete: Center X={self.center_x}, Center Y={self.center_y}")

    def read(self):
        x_value = self.VRx.read() - self.center_x
        y_value = self.VRy.read() - self.center_y
        button_state = self.button.value()
        # Adjust the values so that center is 0,0
        return x_value, y_value, button_state
