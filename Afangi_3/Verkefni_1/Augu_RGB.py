from machine import Pin, PWM
import time

# Initialize RGB pins with PWM for LED 1
red1 = PWM(Pin(16, Pin.OUT), freq=1000)
green1 = PWM(Pin(17, Pin.OUT), freq=1000)
blue1 = PWM(Pin(18, Pin.OUT), freq=1000)

# Initialize RGB pins with PWM for LED 2
red2 = PWM(Pin(7, Pin.OUT), freq=1000)
green2 = PWM(Pin(5, Pin.OUT), freq=1000)
blue2 = PWM(Pin(6, Pin.OUT), freq=1000)

# Function to set color for both LEDs
def set_color(r, g, b):
    red1.duty(r)
    green1.duty(g)
    blue1.duty(b)
    red2.duty(r)
    green2.duty(g)
    blue2.duty(b)

# Example to cycle through some colors
def color_cycle():
    set_color(1023, 0, 0)  # Red
    time.sleep(1)
    set_color(0, 1023, 0)  # Green
    time.sleep(1)
    set_color(0, 0, 1023)  # Blue
    time.sleep(1)

# Run color cycle in a loop
while True:
    color_cycle()

