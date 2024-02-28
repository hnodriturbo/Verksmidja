from machine import Pin
from time import ticks_ms # `ticks_ms` gefur okkur fjölda millisekúnda sem liðnar eru frá því kveikt var að ESP32. 

red = Pin(12, Pin.OUT)
green = Pin(11, Pin.OUT)
takki = Pin(19, Pin.IN, Pin.PULL_UP)

red_kveikt = False 
green_kveikt = False  
takki_stada_adur = 1    

bidtimi = 500                      # ætlum að bíða í 500ms 
timi_lidinn =  ticks_ms()          # skráum upphafspunktinn

while True:
# látum rautt LED blikka
    timi_nuna = ticks_ms()              # skráum hversu langt er síðan ESP ræsti
    if (timi_nuna - timi_lidinn) >= bidtimi:    # True á 500ms fresti 
        red_kveikt = not red_kveikt     # víxlum gildið á boolean
        timi_lidinn = timi_nuna         # uppfærum lidinn tíma í tímann núna fyrir næsta samanburð
    red.value(red_kveikt)               # kveikja/slökkva

# kveikjum á grænt LED með takka 
    takki_stada = takki.value()    
    if takki_stada == 0 and takki_stada_adur == 1:
        green_kveikt = not green_kveikt
    green.value(green_kveikt)
    takki_stada_adur = takki_stada  