# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## ----------------- Created March '24 ----------------- ##
# ###########################################################



from machine import Pin, ADC, SoftI2C
import time
from lib.i2c_lcd import I2cLcd






class Remote:
    def __init__(self, joystick, lcd):
        self.joystick = joystick
        self.lcd = lcd
    
    def update(self):
        while True:
            # Read joystick values
            x, y, button = self.joystick.read()
            
            # Optionally, read MPU data
            # accel = self.mpu.read_acceleration()
            # gyro = self.mpu.read_gyro()
            
            # Display joystick values on LCD
            message = f"X: {x}, Y: {y}"
            self.lcd.display(message)
            if button:
                self.lcd.display("Button Pressed", 1)
            
            time.sleep(0.5)
            
            
    def display_values(self):
        x, y, button = self.joystick.read()
        self.lcd.clear_display()
        button_pressed = 'Yes' if button == 0 else 'No'  # Detect if button is pressed
        self.lcd.display_message(f"X:{x} - Btn Prs:", line=0)
        self.lcd.display_message(f"Y:{y} - - {button_pressed}", line=1)
    
    def test(self):
        while True:
            self.display_values()
            time.sleep(0.5)
