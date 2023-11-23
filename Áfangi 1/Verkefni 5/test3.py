# ----------- Sækjum auka forritasöfn -----------
from machine import Pin, PWM, ADC
# Pin er með grunnstilingar pinna
# PWM gerir pinnum kleyft að skrifa hliðrænt (e. analog)
# ADC gerir vissum pinnum kleyft að lesa hliðrænt.
from time import sleep_ms
import random


# For active-low button with an integrated LED
led_pin_number = 18  # Replace with your actual GPIO pin number
button_pin_number = 13  # Replace with your actual GPIO pin number

# LED setup as an output
led = Pin(led_pin_number, Pin.OUT)

# Button setup as an input with internal pull-up resistor
button = Pin(button_pin_number, Pin.IN, Pin.PULL_UP)

# Later in your code, you can check the button state like this:
if button.value() == 0:  # Button is pressed, pin is LOW
    # Handle button press
    led.value(1)  # Turn on the LED
else:
    led.value(0)  # Turn off the LED
