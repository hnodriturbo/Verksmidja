from machine import Pin, PWM, ADC
from time import sleep_ms
import random

# Setup for LED pins
leds = [Pin(17, Pin.OUT), Pin(16, Pin.OUT), Pin(18, Pin.OUT), Pin(15, Pin.OUT)]

# Setup for button pins
buttons = [Pin(12, Pin.IN, Pin.PULL_UP), Pin(11, Pin.IN, Pin.PULL_UP),
           Pin(13, Pin.IN, Pin.PULL_UP), Pin(10, Pin.IN, Pin.PULL_UP)]

# Speaker setup
speaker = Pin(14, Pin.OUT)
buzzer = PWM(speaker)
buzzer.duty_u16(0)

# Generate a list of 50 random tones
tones = [random.randint(200, 1000) for _ in range(50)]

# Function to play a single tone
def play_tone(tone, duration=200):
    buzzer.freq(tone)
    buzzer.duty_u16(32768)
    sleep_ms(duration)
    buzzer.duty_u16(0)

# Function to turn off all LEDs
def turn_off_leds():
    for led in leds:
        led.value(0)

# Function to light up an LED and play its associated tone
def light_and_tone(led_index, tone):
    leds[led_index].value(1)
    play_tone(tone)
    sleep_ms(200)  # Keep LED on while tone plays
    leds[led_index].value(0)

# Function to play the game sequence
def play_sequence(sequence):
    for led_index in sequence:
        light_and_tone(led_index, tones[led_index])
        sleep_ms(100)  # Wait a bit before the next LED

# Function to get player input
def get_player_input(sequence_length):
    player_sequence = []
    for _ in range(sequence_length):
        while True:
            for i, button in enumerate(buttons):
                if button.value() == 0:  # Button is pressed
                    player_sequence.append(i)
                    light_and_tone(i, tones[i])  # Light and tone for player's button press
                    sleep_ms(300)  # Debounce delay
                    while button.value() == 0:  # Wait for button release
                        sleep_ms(10)
                    break
            sleep_ms(10)
    return player_sequence

# The main game function
def play_game():
    game_sequence = []
    while True:
        # Add a new step to the sequence
        new_step = random.randint(0, 3)
        game_sequence.append(new_step)

        # Play the current game sequence
        play_sequence(game_sequence)

        # Get player input and compare to the game sequence
        player_sequence = get_player_input(len(game_sequence))
        if player_sequence != game_sequence:
            print("Wrong sequence! You lose!")
            for _ in range(4): play_tone(100, 500)  # Play a losing tone
            break  # End the game on a wrong move

        print("Correct sequence! Keep going!")
        sleep_ms(1000)  # Wait before starting the next round

# Start the game
play_game()
