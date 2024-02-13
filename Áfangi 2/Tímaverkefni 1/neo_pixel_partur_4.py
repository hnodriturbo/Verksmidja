from machine import Pin
from neopixel import NeoPixel
import time

neo = NeoPixel(Pin(37), 8)


while True:
    for j in range(2):
        color1 = [255, 0, 0] if j == 0 else [0, 0, 0]
        color2 = [0, 0, 255] if j == 1 else [0, 0, 0]

        for i in range(8):
            if i % 2 == 0:
                neo[i] = color1
            else:
                neo[i] = color2

        neo.write()
        time.sleep(0.5)  # Get auðvitað látið blikka hraðar eða hægar