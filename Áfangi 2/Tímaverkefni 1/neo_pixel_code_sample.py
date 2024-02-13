from machine import Pin
from neopixel import NeoPixel

# búið til nýtt tilvik af NeoPixel klasanum, hringurinn
# er tengdur við pinna 10 og hefur átta perur
neo = NeoPixel(Pin(37), 8)

# litir stilltir með lista [RAUTT, GRÆNT, BLÁTT] þar sem
# hver litur getur tekið gildið frá 0 til og með 255
neo.fill([255, 0, 0]) # Allar perurnar fá sama litinn
neo.write() # Kallað á write til að senda litinn á hringinn

# Einnig hægt að stilla hverja peru sérstaklega
neo[0] = [0, 127, 127]
neo[1] = [63, 63, 63]
neo[2] = [127, 233, 64]
neo.write()