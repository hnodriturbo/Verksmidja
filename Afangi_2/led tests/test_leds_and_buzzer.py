from machine import Pin
from time import sleep

# Set up LEDs
led1 = Pin(11, Pin.OUT)
led2 = Pin(12, Pin.OUT)+
led3 = Pin(13, Pin.OUT)

# Set up the buzzer
buzzer = Pin(3, Pin.OUT)

# Function to test LEDs and buzzer
def test_hardware():
    # Test each LED
    for led in [led1, led2, led3]:
        led.on()
        sleep(1)
        led.off()

    # Test the buzzer
    buzzer.on()
    sleep(1)
    buzzer.off()

# Run the test
test_hardware()
