from machine import Pin, PWM
from time import sleep_ms
import random

class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

class Speaker:
    def __init__(self, pin_number):
        self.speaker = Pin(pin_number, Pin.OUT)
        self.buzzer = PWM(self.speaker)
        self.buzzer.duty_u16(0)  # Start with no sound

    def play_tone(self, tone, duration=200):
        self.buzzer.freq(tone)
        self.buzzer.duty_u16(32768)
        sleep_ms(duration)
        self.buzzer.duty_u16(0)

    def play_sequence(self, tones):
        for tone in tones:
            self.play_tone(tone, 150)
            sleep_ms(100)  # Brief pause between tones

class Button:
    def __init__(self, pin_number):
        self.button = Pin(pin_number, Pin.IN, Pin.PULL_UP)

    def is_pressed(self):
        return self.button.value() == 0

class SimonSaysGame:
    def __init__(self):
        # LED setup
        self.leds = [LED(pin) for pin in [17, 16, 18, 15]]
        # Button setup
        self.buttons = [Button(pin) for pin in [12, 11, 13, 10]]
        # Speaker setup
        self.speaker = Speaker(14)
        
        # Game parameters
        self.tones = [random.randint(200, 1000) for _ in range(30)]
        self.winning_tones = [523, 659, 784, 1047]  # Winning melody
        self.sequence = []
        self.speed = 800  # Start with moderate speed

    def blink_all_leds(self, times=3):
        for _ in range(times):
            self.turn_on_all_leds()
            sleep_ms(200)
            self.turn_off_all_leds()
            sleep_ms(200)

    def turn_on_all_leds(self):
        for led in self.leds:
            led.on()

    def turn_off_all_leds(self):
        for led in self.leds:
            led.off()

    def play_game_sequence(self):
        for index in self.sequence:
            self.leds[index].on()
            self.speaker.play_tone(self.tones[index], 400)
            self.leds[index].off()
            sleep_ms(self.speed)

    def get_player_sequence(self):
        player_sequence = []
        for _ in range(len(self.sequence)):
            button_pressed = False
            while not button_pressed:
                for i, button in enumerate(self.buttons):
                    if button.is_pressed():
                        player_sequence.append(i)
                        self.leds[i].on()
                        self.speaker.play_tone(self.tones[i], 400)
                        self.leds[i].off()
                        button_pressed = True
                        sleep_ms(300)  # Debounce
                        break
                sleep_ms(10)
        return player_sequence

    def play_losing_sequence(self):
        self.turn_on_all_leds()
        self.speaker.play_tone(100, 500)
        self.turn_off_all_leds()
        sleep_ms(500)

    def play_winning_sequence(self):
        for _ in range(4):
            for i in range(len(self.leds)):
                self.leds[i].on()
                self.speaker.play_tone(self.winning_tones[i], 150)
                self.leds[i].off()
                sleep_ms(100)

    def play(self):
        self.blink_all_leds()  # Start the game with a blink sequence

        while True:
            # Add a new random step to the sequence
            new_step = random.randint(0, 3)
            self.sequence.append(new_step)
            
            # Increase speed as the game progresses
            self.speed = max(200, self.speed - 20)

            # Play the current sequence
            self.play_game_sequence()

            # Get and check the player's sequence
            player_sequence = self.get_player_sequence()
            if player_sequence != self.sequence:
                self.play_losing_sequence()
                print("Wrong sequence! Game Over.")
                break

            if len(self.sequence) == 20:  # Winning condition
                print("Congratulations! You've won!")
                self.play_winning_sequence()
                break

            print("Correct sequence! Next round...")
            sleep_ms(1000)  # Pause before the next round

# Start the Simon Says game
game = SimonSaysGame()
game.play()
