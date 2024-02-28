from machine import Pin, PWM, ADC
from time import sleep_ms
import random


# Correct setup for LED pins and Button pins with pull-up configuration
leds = [Pin(17, Pin.OUT), Pin(16, Pin.OUT), Pin(18, Pin.OUT), Pin(15, Pin.OUT)]
buttons = [Pin(12, Pin.IN, Pin.PULL_UP), Pin(11, Pin.IN, Pin.PULL_UP), Pin(13, Pin.IN, Pin.PULL_UP), Pin(10, Pin.IN, Pin.PULL_UP)]


# Speaker setup
speaker = Pin(14, Pin.OUT)
buzzer = PWM(speaker)
buzzer.duty_u16(0)


# Tone definitions
tones = [262, 330, 392, 494]
losing_tones = [440, 349, 294, 220]
winning_tones = [523, 659, 784, 1047]


# Function to play a sequence of tones
def play_tone_sequence(sequence):
    for tone in sequence:
        buzzer.freq(tone)
        buzzer.duty_u16(32768)
        sleep_ms(200)
        buzzer.duty_u16(0)
        sleep_ms(100)


# Function to play a single tone
def play_tone(tone):
    buzzer.freq(tone)
    buzzer.duty_u16(32768)
    sleep_ms(200)
    buzzer.duty_u16(0)


# Wait for input with active-low button configuration
def wait_for_input(led_index, countdown_time):
    while countdown_time > 0:
        if buttons[led_index].value() == 0:  # Button is pressed
            return True
        sleep_ms(10)
        countdown_time -= 10
    return False


# Function to turn off all LEDs
def turn_off_leds():
    for led in leds:
        led.value(0)


# Function to turn on all LEDs constantly
def turn_on_leds():
    for led in leds:
        led.value(1)
        
        
# Function for winning sequence
def win():
    for x in range(4):
        for i in range(len(leds)):
            leds[i].value(1)
            play_tone(winning_tones[i])
            sleep_ms(100)
            leds[i].value(0)
            
            
# The main game function
def play_game():
    while True:
        # Turn off all LEDs at the start of each round
        turn_off_leds()

        # Randomly select one LED to turn on
        led_index = random.randint(0, 3)
        leds[led_index].value(1)  # Turn on only the selected LED

        # Wait for player input and check if the correct button is pressed
        player_correct = wait_for_input(led_index, 2000)

        # Turn off all LEDs after the input period for visual effect
        turn_off_leds()

        if player_correct:
            print("Correct button pressed! You win!")
            win()  # Execute the win routine
        else:
            print("Wrong button or time out! You lose!")
            play_tone_sequence(losing_tones)  # Play the losing sequence

        # Sleep for a bit before the next round starts
        sleep_ms(5000)

# Start the game
play_game()
