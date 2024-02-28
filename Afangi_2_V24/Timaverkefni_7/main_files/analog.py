from machine import Pin, ADC

# pinni 1 skilgreindur sem hliðrænn inntakspinni með 11dB mögnun.
pinni = ADC(Pin(1), atten=ADC.ATTN_11DB)

# sjálfgefið eru ADC 12 bita og gefa því gildi á bilinu 0 til og með 4095
gildi = pinni.read()