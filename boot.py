# boot.py -- run on boot-up
from machine import Pin, PWM, ADC
from time import sleep_ms
import random

# Correct setup for LED pins
#rautt = Pin(16, Pin.OUT)
#graent = Pin(18, Pin.OUT)
#blatt = Pin(15, Pin.OUT)
#gult = Pin(17, Pin.OUT)

# Correct setup for button pins with pull-up configuration
#takki_1 = Pin(11, Pin.IN, Pin.PULL_UP)
#takki_2 = Pin(13, Pin.IN, Pin.PULL_UP)
#takki_3 = Pin(10, Pin.IN, Pin.PULL_UP)
#takki_4 = Pin(12, Pin.IN, Pin.PULL_UP)

# Led's    - Yellow -       - - Red - -        - Green -        - Blue -
leds = [Pin(17, Pin.OUT), Pin(16, Pin.OUT), Pin(18, Pin.OUT), Pin(15, Pin.OUT)]

# Buttons       - Yellow button -            - Red button - 
buttons = [Pin(12, Pin.IN, Pin.PULL_UP), Pin(11, Pin.IN, Pin.PULL_UP),
#               - Green button -             - Blue button - 
           Pin(13, Pin.IN, Pin.PULL_UP), Pin(10, Pin.IN, Pin.PULL_UP)]

# Speaker setup
speaker = Pin(14, Pin.OUT)
buzzer = PWM(speaker)
buzzer.duty_u16(0)



# Generate a list of random tones
tones = [random.randint(200, 1000) for _ in range(30)]
winning_tones = [523, 659, 784, 1047]


# Function to play a single tone
def play_tone(tone, duration=300):
    buzzer.freq(tone)
    buzzer.duty_u16(32768)
    sleep_ms(300)
    buzzer.duty_u16(32768)



# Function to turn off all LED's
def turn_off_all_leds():
    for led in leds:
        led.value(0)



# Function to turn on all LED's
def turn_on_all_leds():
    for led in leds:
        led.value(1)
        
        
            
# Function that lights up an LED and play it's associated tone
def light_and_tone(led_index, tone):
    leds[led_index].value(1) # Light up led
    play_tone(tone) # Play tone
    sleep_ms(1000) # Keep the light and the tone for 1000ms
    leds[led_index].value(0) # Turn off led
    


# Function to play the game sequence
def play_sequence(sequence):
    # Loop through the sequence
    for led_index in sequence:
        light_and_tone(led_index, tones[led_index]) # This selects the light and tone
        sleep_ms(500) # Wait for the next led
    
    
    
def light_up_to_start_game():
    for _ in range(4):
        turn_on_all_leds()
        sleep_ms(200)
        turn_off_all_leds
        sleep_ms(200)
   
# Play the losing sequence
def play_losing_sequence():
    for led in leds:
        led.value(1)
    play_tone(100, 500)
    sleep_ms(500)
    for led in leds:
        led.value(0)
        
# Function for winning sequence
def win():
    for x in range(4):
        for i in range(len(leds)):
            leds[i].value(1)
            play_tone(winning_tones[i])
            sleep_ms(100)
            leds[i].value(0)
        
# Function to get the players input
def get_player_input(sequence_length):
    player_sequence = []
    for _ in range(sequence_length):
        while True:
            for i, button in enumerate(buttons):
                if button.value() == 0: # Button is pressed
                    player_sequence.append(i)
                    light_and_tone(i, tones[i]) # Light and tone for players button press
                    sleep_ms(500) # Debounce delay
                    while button.value() == 0: # Wait for button release
                        sleep_ms(10)
                    break
            sleep_ms(10)
    return player_sequence

# The main game function
def play_game():
    sequence = []
    
    # Blink all the leds 4 times to start a new sequence
    light_up_to_start_game(4)
    
    
    while len(sequence) < 30:
        led_index = random.randint(0, 3)
        sequence.append((led_index, tones[len(sequence)]))

        # Play the sequence
        for seq in sequence:
            light_and_tone(*seq)
            sleep_ms(1000)
        
        # Blink the led's to indicate the player's turn
        light_up_to_start_game()
        
        # Create the player_sequence list
        player_sequence = []
        
        # Player's input
        for _ in sequence:
            while True:
                for i, button in enumerate(buttons):
                    if not button.value():
                        player_sequence.append(i)
                        light_and_tone(i, tones[i])
                        break
                sleep_ms(10)
                if player_sequence[-1] != sequence[len(player_sequence)-1[0]]:
                    play_losing_sequence()
                    print("Wrong sequence! You lose!")
                    return
        print("Correct sequence! Keep going!")
        sleep_ms(5000)
        
    win()
        
play_game()