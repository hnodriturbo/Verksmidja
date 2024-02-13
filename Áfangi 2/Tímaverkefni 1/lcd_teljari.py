from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd
import time

# Initialize the LCD
i2c = SoftI2C(scl=Pin(41), sda=Pin(21), freq=400000)
devices_scan = i2c.scan()  # Assumes only the LCD is connected to I2C

if len(devices_scan) == 0:
    print("Fann ekki skjáinn")
else:
    lcd_address = devices_scan[0]
    # Bý til þá tilvik af skjánum, 2 línur og 16 stafi
    lcd = I2cLcd(i2c, lcd_address, 2, 16)


def telja_upp_og_nidur(lcd, start, end):
    # Telja upp:
    for i in range(start, end + 1):
        lcd.clear() # Byrja a að hreinsa skjáinn
        lcd.move_to(0,0) # Færi bendilinn upp til vinstri
        lcd.putstr(str(i)) # Sýni töluna sem er verið að telja
        time.sleep(0.5) # Tel með hálfra sekónta millibili
    
    for i in range(end, start - 1, -1):
        lcd.clear() # Hreinsa skjáinn
        lcd.move_to(0, 0) # Færi bendilinn
        lcd.putstr(str(i)) # Skrifa töluna á skjáinn
        time.sleep(0.5)
        
# Keyri svo fallið og þá telur þetta upp i 30 og niður frá 30.
telja_upp_og_nidur(lcd, 0, 30)
