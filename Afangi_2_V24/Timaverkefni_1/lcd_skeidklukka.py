from machine import Pin, SoftI2C, Timer
from I2C_LCD import I2cLcd
import time

# Uppsetning
i2c = SoftI2C(scl=Pin(41), sda=Pin(21), freq=400000)
lcd_address = i2c.scan()[0]  # Þar sem þessi skjár er sá eini sem er tengdur vel eg hann strax með 0
lcd = I2cLcd(i2c, lcd_address, 2, 16)


# Takkarnir - Start og stop takkinn ásamt reset takkanum
start_stop_pin = Pin(20, Pin.IN, Pin.PULL_UP)  # Staðsetning takka fyrir byrjun/stöðvun
reset_pin = Pin(19, Pin.IN, Pin.PULL_UP)      # Staðsetning takka fyrir núllstillingu

# Byrja a að stilla inn teljara
counter = 0

# Geri boolean true or false sem segir hvort hann sé í gangi eða ekki
running = False

# Fall sem uppfærir það sem er a skjánum
def update_lcd():
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str(counter))
    
def timer_callback(t):
    # Sæki counter breytuna
    global counter
    # Ef talning er i gangi
    if running:
        # Bæti einn við teljarann
        counter += 1
        # Uppfæri það sem stendur á skjánum
        update_lcd()
        
# Núllum skjáinn strax i byrjun
update_lcd()
  
# Viðurkenni fúslega eg fékk þessar tvær línur á netinu:
timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=timer_callback)


while True:
    
    if not start_stop_pin.value(): # Ef ýtt er á start-stopp takkann
        running = not running
        time.sleep(0.2) # Debounce bið
        
        
    if not reset_pin.value(): # Ef ýtt er a núllstillingu
        counter = 0
        update_lcd()
        time.sleep(0.2)
        
    # Sleep til að minnka cpu notkun var ég að lesa og sá i einu dæminu a netinu
    time.sleep(0.1)