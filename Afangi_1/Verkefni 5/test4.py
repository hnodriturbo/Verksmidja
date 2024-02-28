# ----------- Sækjum auka forritasöfn -----------
from machine import Pin, PWM, ADC
# Pin er með grunnstilingar pinna
# PWM gerir pinnum kleyft að skrifa hliðrænt (e. analog)
# ADC gerir vissum pinnum kleyft að lesa hliðrænt.
from time import sleep_ms
import random

# For active-low button with an integrated LED
led_pin_number = 17  # Replace with your actual GPIO pin number
button_pin_number = 12  # Replace with your actual GPIO pin number

# LED setup as an output
led = Pin(led_pin_number, Pin.OUT)
led.value(1)  # Turn on the LED constantly

# Button setup as an input with internal pull-up resistor
button = Pin(button_pin_number, Pin.IN, Pin.PULL_UP)

# In a loop to check the button state
while True:
    if button.value() == 0:  # Button is pressed, pin is LOW
        print("Button has been pressed!")  # Print message
    sleep_ms(10)  # Small delay to debounce and prevent message spamming
# LED pins
# rautt = Pin(16, Pin.OUT)
# graent = Pin(18, Pin.OUT)
# blatt = Pin(15, Pin.OUT)
# gult = Pin(17, Pin.OUT)

# Button pins with pull-up configuration
# takki_1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
# takki_2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
# takki_3 = Pin(10, Pin.IN, Pin.PULL_DOWN)
# takki_4 = Pin(12, Pin.IN, Pin.PULL_DOWN)