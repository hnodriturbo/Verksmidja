# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## ----------------- Created March '24 ----------------- ##
# ###########################################################



from machine import Pin, ADC, SoftI2C
import time
from lib.i2c_lcd import I2cLcd

# Import component classes and configuration
from remote_files.settings import config
from remote_files.joystick import Joystick
from remote_files.lcd import LCD
from remote_files.remote import Remote

# Initialize components with settings from config
joystick = Joystick(VRx_pin=config['joystick']['VRx_pin'], 
                    VRy_pin=config['joystick']['VRy_pin'], 
                    button_pin=config['joystick']['button_pin'])

lcd = LCD(lcd_i2c_address=config['lcd']['lcd_i2c_address'], 
          sda_pin=config['lcd']['sda_pin'], 
          scl_pin=config['lcd']['scl_pin'])

# Create the Remote instance with the components
remote_control = Remote(joystick=joystick, lcd=lcd)

# Run the test to display joystick values and button status on the LCD
remote_control.test()










