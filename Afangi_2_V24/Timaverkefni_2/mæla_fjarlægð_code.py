from machine import Pin
from time import sleep_ms, sleep_us, ticks_us, ticks_diff

echo = Pin(47, Pin.IN)
trig = Pin(48, Pin.OUT)

def maela_fjarlaegd():
    # Sendum 10 míkrosekúndna púls
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    
    # Bíðum eftir að svarpúlsinn byrji
    while not echo.value(): # eða echo.value() == 0
        pass # Ekkert að gera nema bíða
    
    # Svarpúlsinn er byrjaður að berast þannig að við setjum skeiðklukku í gang
    upphafstimi = ticks_us()
    
    # Bíðum eftir að svarpúlsinn endi
    while echo.value(): # eða echo.value() == 1
        pass # Ekkert að gera nema bíða
    
    # Svarpúlsinn er ekki lengur að berast þannig að við stoppum skeiðklukkuna
    endatimi = ticks_us()
    
    # Reiknum muninn á upphafs og endatímanum
    heildartimi = ticks_diff(endatimi, upphafstimi)
    
    # Notum svo helildartímann til að reikna út fjarlægðina skv. jöfnunni fjarlægð = hraði * tími
    # byrjum á að helminga heildartímann (merkið fer fram og til baka)
    heildartimi /= 2
    # Hljóðhraðinn er 340 m/s (34000 cm/s) og svo deilum við með 1000000 til að fá cm á míkrósekúndur.
    hljodhradi = 34000 / 1000000
    # Reiknum loks fjarlægðina í cm
    fjarlaegd = heildartimi * hljodhradi
    
    # Skilum svo fjarlægðinni sem heiltölu sem er næg nákvæmni
    return int(fjarlaegd)
    

while True:
    fjarlaegd = maela_fjarlaegd()
    print(f"Mæld fjarlægð: {fjarlaegd}")
    sleep_ms(500)

