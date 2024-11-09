from machine import Pin, PWM
import time

class Speaker:
    def __init__(self, pin):
        # Initialize the speaker pin as a PWM output
        self.speaker = Pin(pin, Pin.OUT)
        self.buzzer = PWM(self.speaker)
        self.buzzer.duty_u16(0)  # Start with no sound

    def play_tone(self, tone, duration=200):
        """
        Play a single tone at a specified frequency (tone) for a given duration in milliseconds.
        """
        if tone > 0:
            # Only play if the tone frequency is valid (non-zero)
            self.buzzer.freq(tone)         # Set the frequency of the tone
            self.buzzer.duty_u16(32768)    # Set duty to 50% for audible sound
            time.sleep_ms(duration)        # Play the tone for the specified duration
            self.buzzer.duty_u16(0)        # Turn off sound after the duration
        else:
            # If tone is 0, it's a rest, so just wait for the duration
            time.sleep_ms(duration)

    def play_sequence(self, tones):
        """
        Play a sequence of tones, with a brief pause between each.
        """
        
        # Sample sequence of random tones (frequencies in Hz) to play
        tones = [440, 494, 523, 587, 659, 698, 784] # List of tones
        
        for tone in tones:
            self.play_tone(tone, 200)
            time.sleep_ms(100)  # Brief pause between tones
            
            
    def play_sequence_back_and_forth(self, tones):
        """
        Play a sequence of tones forward, then reverse, in an infinite loop.
        """
        # Sample sequence of random tones (frequencies in Hz) to play
        tones = [440, 494, 523, 587, 659, 698, 784] # List of tones
        
        direction = 1  # 1 for forward, -1 for backward
        
        while True:
            # Play tones in the current direction
            for tone in tones[::direction]:
                self.play_tone(tone, 200)
                time.sleep_ms(100)  # Brief pause between tones
            
            # Reverse direction after each cycle
            direction *= -1
            
            
    # Mario bros theme song !!!
    def play_mario_theme(self):
        """
        Play the Super Mario Bros. theme song.
        """
        # Define the melody: (frequency in Hz, duration in ms)
        melody = [
            (659, 150), (659, 150), (0, 150), (659, 150), (0, 100), (523, 150), (659, 150), (0, 150), (784, 150), (0, 375),
            (392, 150), (0, 375), (523, 150), (0, 250), (392, 150), (0, 250), (330, 150), (0, 250), (440, 150), (0, 150),
            (494, 150), (0, 150), (466, 150), (440, 150), (0, 150), (392, 150), (659, 150), (784, 150), (880, 150), (0, 150),
            (698, 150), (784, 150), (0, 150), (659, 150), (0, 150), (523, 150), (587, 150), (494, 150), (0, 150),
            (523, 150), (0, 250), (392, 150), (0, 250), (330, 150), (0, 250), (440, 150), (0, 150), (494, 150), (0, 150),
            (466, 150), (440, 150), (0, 150), (392, 150), (659, 150), (784, 150), (880, 150), (0, 150), (698, 150), (784, 150),
            (0, 150), (659, 150), (0, 150), (523, 150), (587, 150), (494, 150), (0, 375), (784, 150), (740, 150), (698, 150),
            (622, 150), (659, 150), (0, 150), (415, 150), (440, 150), (523, 150), (0, 150), (440, 150), (523, 150), (587, 150),
            (0, 150), (784, 150), (740, 150), (698, 150), (622, 150), (659, 150), (0, 150), (698, 150), (698, 150), (698, 150),
            (0, 150), (784, 150), (740, 150), (698, 150), (622, 150), (659, 150), (0, 150), (415, 150), (440, 150), (523, 150),
            (0, 150), (440, 150), (523, 150), (587, 150), (0, 150), (622, 150), (0, 150), (587, 150), (523, 150), (0, 150),
            (494, 150), (0, 150), (523, 150), (0, 250), (392, 150), (0, 250), (330, 150), (0, 250), (440, 150), (0, 150),
            (494, 150), (0, 150), (466, 150), (440, 150), (0, 150), (392, 150), (659, 150), (784, 150), (880, 150), (0, 150),
            (698, 150), (784, 150), (0, 150), (659, 150), (0, 150), (523, 150), (587, 150), (494, 150), (0, 375), (784, 150),
            (740, 150), (698, 150), (622, 150), (659, 150), (0, 150), (415, 150), (440, 150), (523, 150), (0, 150), (440, 150),
            (523, 150), (587, 150), (0, 150), (784, 150), (740, 150), (698, 150), (622, 150), (659, 150), (0, 150), (698, 150),
            (698, 150), (698, 150), (0, 150), (784, 150), (740, 150), (698, 150), (622, 150), (659, 150), (0, 150), (415, 150),
            (440, 150), (523, 150), (0, 150), (440, 150), (523, 150), (587, 150)
        ]

        # Play each note in the melody
        for frequency, duration in melody:
            self.play_tone(frequency, duration)
            
    def play_happy_birthday(self):
        melody = [
            (264, 250), (264, 250), (297, 500), (264, 500), (352, 500), (330, 1000),
            (264, 250), (264, 250), (297, 500), (264, 500), (396, 500), (352, 1000),
            (264, 250), (264, 250), (528, 500), (440, 500), (352, 250), (330, 250), (297, 750),
            (466, 250), (466, 250), (440, 500), (352, 500), (396, 500), (352, 1000)
        ]
        for tone, duration in melody:
            self.play_tone(tone, duration)

# Initialize speaker on pin 10
speaker = Speaker(pin=10)



# Play the sequence
while True:
    speaker.play_happy_birthday()

