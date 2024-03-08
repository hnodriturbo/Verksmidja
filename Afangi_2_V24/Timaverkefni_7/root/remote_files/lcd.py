# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## ----------------- Created March '24 ----------------- ##
# ###########################################################



from machine import Pin, ADC, SoftI2C
import time
from lib.i2c_lcd import I2cLcd

class LCD:
    def __init__(self, lcd_i2c_address, sda_pin, scl_pin):
        """
        Initializes the LCD display with I2C communication.
        
        :param lcd_i2c_address: The I2C address of the LCD.
        :param sda_pin: The pin number used for I2C SDA.
        :param scl_pin: The pin number used for I2C SCL.
        """
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
        self.lcd = I2cLcd(self.i2c, lcd_i2c_address, 2, 16)

    def clear_display(self):
        """Clears the LCD display."""
        self.lcd.clear()

    def display_message(self, message, line=0):
        """
        Displays a message on the LCD.
        
        :param message: The message to display.
        :param line: The line number (0 or 1) to display the message on.
        """
        if line not in [0, 1]:
            raise ValueError("Line must be 0 or 1.")
        self.lcd.move_to(0, line)
        self.lcd.putstr(message)

    def test_display(self):
        """Runs a series of tests to display messages on the LCD."""
        self.clear_display()
        self.display_message("LCD Test", line=0)
        time.sleep(2)  # Wait for 2 seconds

        self.clear_display()
        self.display_message("Line 1", line=0)
        self.display_message("Line 2", line=1)
        time.sleep(2)  # Wait for 2 seconds

        # Scroll text on the first line
        self.clear_display()
        for position in range(16):
            self.lcd.move_to(position, 0)
            self.lcd.putstr("Scroll")
            time.sleep(0.3)
            self.clear_display()

        # Display complete
        self.display_message("Test Done", line=0)

# # Example usage
# if __name__ == '__main__':
#     lcd = LCD(lcd_i2c_address=0x3F, sda_pin=40, scl_pin=39)
#     lcd.test_display()
