from machine import Pin
from time import sleep_ms

# Byrja a að skrilgreina breytur og pinna
graent = Pin(10, Pin.OUT) # Pinni 10 skilgreindur sem úttakspinni (stafrænn)
blatt = Pin(11, Pin.OUT) # Pinni 11 skilgreindur sem úttakspinni (stafrænn)
takki_a = Pin(12, Pin.IN, Pin.PULL_UP) # Pinni 12 skilgr. sem inntakspinni (stafrænn)

# Stilli upphafsstöðu
graent.value(0)
blatt.value(1)


# A liður verkefnisins

#while True:
#    graent.value(0)
#    blatt.value(1)
    
#    sleep_ms(250)
    
#    graent.value(1)
#    blatt.value(0)
    
#    sleep_ms(250)
    
# B liður verkefnisins
while True:
    if takki_a.value() == 0: # afþví takki er Pin.PULL_UP er þegar ýtt a hann gildið 0
        graent.value(0)
        blatt.value(1)
        
        sleep_ms(250)
        
        graent.value(1)
        blatt.value(0)
        
        sleep_ms(250)
    # Ef takkinn er ekki þrýstur niður er slökkt:
    else:
        graent.value(0)
        blatt.value(0)
        