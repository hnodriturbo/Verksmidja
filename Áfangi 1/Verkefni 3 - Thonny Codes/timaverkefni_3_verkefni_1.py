# ----------- Sækjum auka forritasöfn -----------
from machine import Pin, PWM, ADC
# Pin er með grunnstilingar pinna
# PWM gerir pinnum kleyft að skrifa hliðrænt (e. analog)
# ADC gerir vissum pinnum kleyft að lesa hliðrænt.
from time import sleep_ms
# sleep_ms frystir forrit í ákveðið margar millisekúndur

# ----------- Skilgreinum breytur og pinna -----------
rautt = Pin(9, Pin.OUT) # Pinni 9 skilgreindur sem úttakspinni (stafrænn)
graent = Pin(10, Pin.OUT) # Pinni 10 skilgr. sem úttakspinni (stafrænn)
blatt = PWM(Pin(11), freq=10000) # Pinni 11 skilgr. sem úttakspinni (hliðrænn)
takki_a = Pin(12, Pin.IN, Pin.PULL_UP) # Pinni 12 skilgr. sem inntakspinni (stafrænn)
takki_b = Pin(13, Pin.IN, Pin.PULL_DOWN) # Pinni 13 skilgr. sem inntakspinni (stafrænn)
stillividnam = ADC(Pin(14), atten=ADC.ATTN_11DB) # Pinni 14 skilgr. sem inntakspinni (hliðrænn)
hatalari_active = Pin(7, Pin.OUT) # Pinni 7 skilgreindur sem úttakspinni (stafrænn)
hatalari_passive = PWM(Pin(8), freq=10000) # Pinni 8 skilgr. sem úttakspinni (hliðrænn)

# ----------- Lykkjan þar sem virknin er útfærð -----------
while True:
    rautt.value(1) # Skrifum 3.3V á pinna 9
    graent.value(1) # Skrifum 3.3V á pinna 9
    
    # Lesum stöðuna á stilliviðnáminu og geymum í breytu, það gefur 
    # okkur tölu á bilinu 0 til 4096 sem er spenna á bilinu 0 - 3.3V.
    stillividnam_stada = stillividnam.read()
    # Skrifum 0 - 3.3V á pinna 11. PWM getur bara unnið með tölur á bilinu 
    # 0 til 1023 en stilliviðnámið gaf okkur tölu á bilinu 0 til 4096. Við 
    # deilum því með 4 í töluna og pössum að það sé heiltöludeiling.
    blatt.duty(stillividnam_stada // 4)
    
    # Spyrjum hvort að staðan á pinna 12 sé 0 (PULL_UP hér að ofan 
    # gerir það að verkum að pinninn er alltaf með stöðuna 1 (3.3V))
    if takki_a.value() == 0:
        # Ef svo er skrifum við 3.3V á pinna 7
        hatalari_active.value(1)
    else:
        # Ef svo er ekki skrifum við 0V á pinna 7
        hatalari_active.value(0)
        
    # Spyrjum hvort að staðan á pinna 12 sé 1 (PULL_DOWN hér að ofan 
    # gerir það að verkum að pinninn er alltaf með stöðuna 0 (0V))
    if takki_b.value() == 1:
        # Ef svo er stillum við PWM duty cycle á 50%
        hatalari_passive.duty(512)
        # Setjum tíðnina á PWM á 440Hz (A nóta)
        hatalari_passive.freq(440)
        # Bíðum í hálfa sekúndu
        sleep_ms(500)
        # Setjum svo PWM tíðnina á 523Hz (C nóta)
        hatalari_passive.freq(523)
        # Bíðun svo í hálfa sekúndu
        sleep_ms(500)
    else:
        # Ef svo er ekki stillum við PWM duty cycle á 0%
        hatalari_passive.duty(0)

