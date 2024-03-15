from machine import Pin, ADC, SoftI2C
import time
from lib.i2c_lcd import I2cLcd

# Joystick Pins
VRx_PIN = 5
VRy_PIN = 6
BUTTON_PIN = 7

# LCD setup
LCD_I2C_ADDRESS = 0x3F
i2c = SoftI2C(scl=Pin(39), sda=Pin(40), freq=100000)
lcd = I2cLcd(i2c, LCD_I2C_ADDRESS, 2, 16)

# Initialize ADC for joystick's X and Y axes
# x_axis = ADC(Pin(VRx_PIN), atten=ADC.ATTN_11DB)
# y_axis = ADC(Pin(VRy_PIN), atten=ADC.ATTN_11DB)
x_axis = ADC(Pin(VRx_PIN), atten=ADC.ATTN_11DB)
y_axis = ADC(Pin(VRy_PIN), atten=ADC.ATTN_11DB)
# Initialize the joystick button
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def display_values(x, y, button):
    lcd.clear()
    button_pressed = 'Yes' if button == 0 else 'No'  # Detect if button is pressed
    lcd.putstr(f"X:{x} - Btn Prs:")
    lcd.move_to(0, 1)  # Move to the second line
    lcd.putstr(f"Y:{y} - - {button_pressed}")  # Display button status

while True:
    # Read joystick values
    x_value = x_axis.read()
    y_value = y_axis.read()
    button_state = button.value()
    
    # Display values on LCD
    display_values(x_value, y_value, button_state)
    
    # Also print the values to the console for debugging
    print(f"X: {x_value}, Y: {y_value}, Button: {button_state}")
    
    # Delay to make it readable and not too fast
    time.sleep(0.5)
