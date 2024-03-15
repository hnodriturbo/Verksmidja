from machine import Pin, SoftI2C
import time

# Import the library for the LCD
# Make sure to have the necessary libraries uploaded to your ESP32
# The name of the library may differ; ensure it is correct
# from i2c_lcd import I2cLcd
# from i2c_lcd import *
from lib.i2c_lcd import I2cLcd

# The I2C address for a 1602 LCD with I2C interface is usually 0x27.
# If your display has a different address, you will need to adjust it.
# LCD_I2C_ADDRESS = 0x27
LCD_I2C_ADDRESS = 0x3F  


# Initialize the I2C interface on the ESP32 using software I2C
# Make sure to specify the correct pins for SDA and SCL
i2c = SoftI2C(scl=Pin(39), sda=Pin(40), freq=100000)

# Scan for devices on the I2C bus and print their addresses
print('Scanning I2C bus...')
devices = i2c.scan()
if devices:
    for device in devices:
        print("I2C device found at address: 0x{:02X}".format(device))
else:
    print("No I2C device found. Check your connections.")

# Initialize the LCD using the I2C connection
lcd = I2cLcd(i2c, LCD_I2C_ADDRESS, 2, 16)
# Initialize the LCD using the I2C connection with the correct address
lcd = I2cLcd(i2c, LCD_I2C_ADDRESS, 2, 16)



while True:
    # Clear the LCD and print a test message
    lcd.clear()  # Clear any text that might be on the screen
    lcd.putstr(" Hello, World !")  # Print a test message on the first line

    # Wait a couple of seconds to see the message
    time.sleep(1)

    # If you want to display more text or move to the second line, use:
    lcd.move_to(0, 1)  # Move cursor to the beginning of the second line
    lcd.putstr(" Fuck off ! ! !")  # Print a test message on the second line

    # Keep the message displayed
    time.sleep(1)





