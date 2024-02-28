from machine import Pin
from time import sleep_ms

takki_a = Pin(12, Pin.IN, Pin.PULL_UP) # Pinni 12 skilgr. sem inntakspinni (stafrænn)
rautt_led = Pin(9, Pin.OUT) # Pinni 9 skilgreindur sem úttakspinni (stafrænn)

# Bæti við takka B og bláu led
takki_b = Pin(13, Pin.IN, Pin.PULL_DOWN) # Pinni 13 skilgr. sem inntakspinni (stafrænn)
blatt_led = Pin(11, Pin.OUT) # Pinni 11 skilgreindur sem úttakspinni (stafrænn)



# Rauð pera boolean og breyta sem geymir stöðuna
ljos_kveikt_rautt = False # Ákveð að ljósið byrji slökkt
takki_stada_adur_rautt = 1 # Breytan geymir stöðuna a takkanum i síðustu umferð

# Bæti við sama fyrir bláu peruna
ljos_kveikt_blatt = False
takki_stada_adur_blatt = 0

while True:
    
    # Kóðinn fyrir rauðu peruna og takka A
    takki_stada_rautt = takki_a.value() # les takkann i breytuna takki_stada
    
    if takki_stada_adur_rautt == 1 and takki_stada_rautt == 0:
        ljos_kveikt_rautt = not ljos_kveikt_rautt
        
    rautt_led.value(ljos_kveikt_rautt)
    
    takki_stada_adur_rautt = takki_stada_rautt
    
    

        # Kóðin fyrir bláu peruna og takka B
    takki_stada_blatt = takki_b.value() # Les takkann í breytuna
    if takki_stada_adur_blatt == 0 and takki_stada_blatt == 1:
        ljos_kveikt_blatt = not ljos_kveikt_blatt
    blatt_led.value(ljos_kveikt_blatt)
    takki_stada_adur_blatt = takki_stada_blatt
    
    # Bæti við smá sleep_ms - kóðinnn virkaði ekki fyrir bláu fyrr en ég setti sleep_ms inn
    sleep_ms(50)