from machine import Pin
from time import sleep

# Initialize the buttons with built-in LEDs
button_leds = [
    Pin(11, Pin.OUT),  # Red button LED
    Pin(13, Pin.OUT),  # Green button LED
    Pin(10, Pin.OUT), # Blue button LED
    Pin(12, Pin.OUT), # Yellow button LED
]

# Initialize the buttons
buttons = [
    Pin(16, Pin.IN, Pin.PULL_UP),  # Red button
    Pin(18, Pin.IN, Pin.PULL_UP),  # Green button
    Pin(15, Pin.IN, Pin.PULL_UP), # Blue button
    Pin(17, Pin.IN, Pin.PULL_UP), # Yellow button
]

# Test the button LEDs
while True:
    for i in range(len(buttons)):
        if buttons[i].value() == 1:  # Check if button is pressed
            button_leds[i].on()      # Turn on the LED
        else:
            button_leds[i].off()     # Turn off the LED

    sleep(0.1)  # Small delay to debounce buttons
