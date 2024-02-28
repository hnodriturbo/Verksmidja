from machine import Pin
from neopixel import NeoPixel
import time

neo = NeoPixel(Pin(37), 8)

def afram():
    for i in range(8):
        neo.fill([0, 0, 0]) # Slökkva á öllum led perunum
        neo[i] = [0, 255, 0] # Lýsa upp ljós sem i er.. lúppar frá 1 upp í 8
        neo.write()
        time.sleep(0.5) # Skipti um peru a hálfra sekóntu fresti
    
def afturabak():
    for i in range(7, -1, -1):
        neo.fill([0, 0, 0]) # Slökkva á öllum led perunum
        neo[i] = [0, 255, 0] # Lýsa upp ljós sem i er.. lúppar frá 1 upp í 8
        neo.write()
        time.sleep(0.5) # Skipti um peru a hálfra sekóntu fresti
    
# Keyri föllin svo    
afram()
afturabak()


#while True:
#    for i in range(8):
#        neo.fill([0, 0, 0]) # Slökkva á öllum led perunum
#        neo[i] = [0, 255, 0] # Lýsa upp ljós sem i er.. lúppar frá 1 upp í 8
#        neo.write()
#        time.sleep(0.5) # Skipti um peru a hálfra sekóntu fresti
        
## Til þess að láta perurnar fara í öfuga átt get eg látið "for" lúppuna
## ganga frá 7 og niðrí 0 með því að gera 7, -1, -1
        
#while True:
#    for i in range(7, -1, -1):
#        neo.fill([0, 0, 0]) # Slökkva á öllum led perunum
#        neo[i] = [0, 255, 0] # Lýsa upp ljós sem i er.. lúppar frá 1 upp í 8
#        neo.write()
#        time.sleep(0.5) # Skipti um peru a hálfra sekóntu fresti