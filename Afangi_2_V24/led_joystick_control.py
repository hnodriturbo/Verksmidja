from machine import Pin, ADC, PWM
import time
from time import sleep_ms

x_axis = ADC(Pin(9), atten=ADC.ATTN_11DB)
y_axis = ADC(Pin(8), atten=ADC.ATTN_11DB)
button = Pin(7, Pin.IN, Pin.PULL_UP)


led = PWM(Pin(45), freq=5000)

led_on = False
last_button_press = 0 # Timestamp of the last button press



def get_let_duty(y_value):
    
    return (4095 - y_value) * 1023 // 4095

while True:
    current_time =  time.ticks_ms()
    y_value = y_axis.read()
    button_state = button.value()
    
    # Simple button debounce
    if not button_state and current_time - last_button_press > 200:
        led_on = not led_on
        last_button_press = current_time
        
    if led_on:
        duty = get_let_duty(y_value)
        led.duty(duty)
    else:
        led.duty(0)
    
    sleep_ms(100)


# 
# while True:
#     print(f"X: {x_as.read()}, Y: {y_as.read()}, Takki: {takki.value()}")
#     sleep_ms(500)