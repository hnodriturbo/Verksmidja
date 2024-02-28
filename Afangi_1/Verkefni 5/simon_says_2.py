from machine import Pin, PWM, ADC
from time import sleep_ms
import random

# ... (Your existing setup code goes here)

# Generate a list of 50 tones
extended_tones = [random.randint(200, 1000) for _ in range(50)]

# Function to play a sequence of tones with associated LED
def play_sequence(sequence):
    for led_index, tone in sequence:
        leds[led_index].value(1)  # Turn on the LED
        play_tone(tone)  # Play the associated tone
        leds[led_index].value(0)  # Turn off the LED
        sleep_ms(100)

# Modified game function for Simon Says
def simon_says_game():
    sequence = []  # Initialize the sequence list

    while True:
        # Add a new step to the sequence
        led_index = random.randint(0, 3)
        tone = random.choice(extended_tones)
        sequence.append((led_index, tone))

        # Play the sequence for the player
        play_sequence(sequence)

        # Player's turn to repeat the sequence
        for led_index, tone in sequence:
            if not wait_for_input(led_index, 2000):
                # Wrong button or timeout
                print("Wrong button or time out! You lose!")
                play_tone_sequence(losing_tones)  # Play the losing sequence
                return  # End the game if the player is wrong

            # If the correct button was pressed, play the associated tone and light
            leds[led_index].value(1)
            play_tone(tone)
            leds[led_index].value(0)

        # Player got the sequence right
        print("Correct sequence! Next round...")
        sleep_ms(1000)

# Start the Simon Says game
simon_says_game()
