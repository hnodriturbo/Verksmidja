from machine import Pin, ADC # Importa Pin og ADC
from time import sleep_ms # Importa sleep_ms

# Stilli pinna 14 sem stillividnam
stillividnam = ADC(Pin(14), atten=ADC.ATTN_11DB) # Pinni 14 skilgr. sem inntakspinni (hliðrænn)

# Skilgreini rauðu peruna
rautt_led = Pin(9, Pin.OUT) # Rauða led peran í pinna 9

# Bilið á blikkinu
blikk_rate = 0 # Skilgreini blikk_rate


# Endlausa lúppan
while True:
    # Les stöðuna i breytuna
    stillividnam_stada = stillividnam.read()
    
    # Ég fann út að stilliviðnám gefur gildi frá 0 upp i 4095 þannig ég deildi bara með 4
    blikk_rate = int(stillividnam_stada / 4)
    
    # Toggla rauðu peruna af og a með þessari línu
    rautt_led.value(not rautt_led.value())
    
    # Stilli sleep_ms af blikk_rate
    sleep_ms(blikk_rate)
    