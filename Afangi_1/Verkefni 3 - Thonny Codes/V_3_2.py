# Sækja auka forritasöfn. Þurfum Pin, PWM og sleep_ms
from machine import Pin, PWM, ADC
from time import sleep_ms
# Skilgreina pinnann sem rauða peran er tengd við sem PWM
rautt_led = PWM(Pin(9), freq=10000)
# þurfum breytu sem heldur utan um birtumagnið á hverjum tíma og getur hækkað og lækkað
birtumagn = 0
# Breyta sem veit hvort ljósmagnið á að aukast eða minnka
birtir = True

while True:
    # skrifa birtumagnið á rauða LED
    rautt_led.duty(birtumagn)
    # ef ljósmagnið á að aukast
    if birtir:
        # hækka þá birtumagns breytuna um 1
        birtumagn += 1
    # annars
    else:
        # lækka birtumagns breytuna um 1
        birtumagn -= 1
    # ef birtumagn er 0 eða birtumagn er 1024
    if birtumagn == 0 or birtumagn == 1023:
        # snúa birtir breytunni við ef hún er True á hún að verða False og svo öfugt
        if birtir:
            birtir = not birtir
        else:
            birtir = True
    # bíða (sleep_ms) í örfáar (minna en 5) millisekúndur
    sleep_ms(2)
    
    
# ----- Hérna er önnur útgáfa af þessu sama sem ég uppfærði ---- #
# ----- Finnst þessi einfaldari ---- #
while True:
    rautt_led.duty(birtumagn)
    if birtir:
        if birtumagn < 1023:
            birtumagn += 1
        else:
            birtir = False
    else:
        if birtumagn > 0:
            birtumagn -= 1
        else:
            birtir = True
    sleep_ms(2)