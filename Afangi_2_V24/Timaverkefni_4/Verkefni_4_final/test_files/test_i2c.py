from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(45), sda=Pin(21))
devices = i2c.scan()
print("I2C devices found:", devices)