from machine import Pin
from neopixel import NeoPixel
import time

neo = NeoPixel(Pin(37), 8)

while True:
    # Setjum öll ljós a rauð
    neo.fill([255, 0, 0])
    neo.write()
    time.sleep(2) # Bíð 2 sekóntur
    
    # Setjum öll ljós yfir á blá ljós
    neo.fill([0, 0, 255])
    neo.write()
    time.sleep(2) # Bíð 2 sekóntur
    
    # Lúppar
    