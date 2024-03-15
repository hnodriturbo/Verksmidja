from machine import Pin, ADC
from time import sleep_ms

x_as = ADC(Pin(5), atten=ADC.ATTN_11DB)
y_as = ADC(Pin(6), atten=ADC.ATTN_11DB)
takki = Pin(7, Pin.IN, Pin.PULL_UP)

while True:
    print(f"X: {x_as.read()}, Y: {y_as.read()}, Takki: {takki.value()}")
    sleep_ms(500)