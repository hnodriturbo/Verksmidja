from machine import Pin
from time import sleep

# Button pins with pull-up configuration
takki_1 = Pin(3, Pin.IN, Pin.PULL_UP)
takki_2 = Pin(16, Pin.IN, Pin.PULL_UP)
takki_3 = Pin(17, Pin.IN, Pin.PULL_UP)
takki_4 = Pin(18, Pin.IN, Pin.PULL_UP)

buttons = [takki_1, takki_2, takki_3, takki_4]

while True:
    for i, button in enumerate(buttons):
        if not button.value():
            print(f"Button {i+1} pressed")
    sleep(0.1)  # Simple debounce
    
    
    
# grænn 1 og 2

# rauður 4 og 5

# blár 47 48

# gulur 10 11

# buzzer 14