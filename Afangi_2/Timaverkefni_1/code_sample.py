from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd

# Skjárinn nota I2C tengingu til að tala við ESP
i2c = SoftI2C(scl=Pin(41), sda=Pin(21), freq=400000)

# Mörg tæki geta notað sömu tenginguna, 
# scan skilar lista af öllum tækjunum sem fundust
taekin = i2c.scan()

# Við erum bara með eitt tæki (skjáinn)
if len(taekin) == 0:
    print("Fann ekki skjáinn")
else:
    # búum til tilvik af skjánum, skjárinn 
    # hefur 2 línur og 16 stafi í hvorri línu
    lcd = I2cLcd(i2c, taekin[0], 2, 16)

# Færi bendilinn í staf nr. 0 og línu nr. 0
lcd.move_to(0, 0)
lcd.putstr("Hallo")
# Færi bendilinn í staf nr. 0 og línu nr. 1
lcd.move_to(0, 1)
lcd.putstr("Heimur")

# Skoðaðu skrána LCD_API.py til að kynna þér önnur föll sem 
# hægt er að nota með LCD skjánum