from machine import Pin
import neopixel
import time

# Number of LEDs in your ring
num_leds = 8  # Adjust this number if your ring has a different number of LEDs

# Create a NeoPixel object on GPIO2 (or another pin you choose)
np = neopixel.NeoPixel(Pin(2), num_leds)

# Function to light up each LED in sequence
def run_sequence():
    for i in range(num_leds):
        np[i] = (255, 0, 0)  # Set to Red color (you can change the color)
        np.write()
        time.sleep(0.5)
        np[i] = (0, 0, 0)  # Turn off
        np.write()

# Run the sequence
while True:
    run_sequence()
