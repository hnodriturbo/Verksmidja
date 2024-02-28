from machine import Pin, SoftI2C, Timer
from I2C_LCD import I2cLcd
from neopixel import NeoPixel
import time
import random

# Setup
i2c = SoftI2C(scl=Pin(41), sda=Pin(21), freq=400000)
lcd_address = i2c.scan()[0]
lcd = I2cLcd(i2c, lcd_address, 2, 16)
neo = NeoPixel(Pin(37), 8)  # NeoPixel connected to pin 37

# Buttons (Wires)
wire_1 = Pin(20, Pin.IN, Pin.PULL_UP)
wire_2 = Pin(19, Pin.IN, Pin.PULL_UP)
wire_3 = Pin(18, Pin.IN, Pin.PULL_UP)

# Initialize countdown
counter = 60
running = True
speed = 1000

# Randomize hvað er réttur vír og ekki
correct_wire = random.choice([wire_1, wire_2, wire_3])


# Uppfæra það sem stendur á skjánum
def update_lcd():
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(f"Time: {counter}")


# Niðurteljari
def timer_callback(t):
    global counter
    if running and counter > 0:
        counter -= 1
        update_lcd()
        # Ef teljari nær 0 þá keyrist þú tapar fallið, rauð ljós og boom stendur a skjánum
        if counter == 0:
            you_lose()
            
            
# Vildi gera þú tapar fall og þú vinnur fall
def you_win():
    global running
    running = False
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("YOU WIN!")
    blink_neopixel([0, 255, 0])  # Grænn

# Vildi gera þú tapar fall og þú vinnur fall
def you_lose():
    global running
    running = False
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("BOOOOOM!")
    blink_neopixel([255, 0, 0])  # Rauður

# Auðveldawra víst ég nota blikkandi neopixel i tveimur öðrum föllum að gera
# blikkið að sérstöku falli
def blink_neopixel(color):
    for _ in range(5):
        neo.fill(color)
        neo.write()
        time.sleep(0.5)
        neo.fill([0, 0, 0])
        neo.write()
        time.sleep(0.5)

def check_wire(wire):
    global speed
    if wire is correct_wire:
        you_win()
    else:
        speed = speed // 2
        timer.init(period=speed, mode=Timer.PERIODIC, callback=timer_callback)

timer = Timer(-1)
timer.init(period=speed, mode=Timer.PERIODIC, callback=timer_callback)
update_lcd()

while True:
    if not wire_1.value():
        check_wire(wire_1)
        time.sleep(0.2)
    if not wire_2.value():
        check_wire(wire_2)
        time.sleep(0.2)
    if not wire_3.value():
        check_wire(wire_3)
        time.sleep(0.2)
    time.sleep(0.1)