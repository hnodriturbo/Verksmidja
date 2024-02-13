from machine import Pin, PWM
import time

# Initialize the passive buzzer
buzzer = PWM(Pin(3), freq=440, duty=512)  # 440 Hz frequency, 50% duty cycle

def play_tone(frequency, duration_ms):
    buzzer.freq(frequency)
    buzzer.duty(512)  # 50% duty cycle to turn on the buzzer
    time.sleep_ms(duration_ms)
    buzzer.duty(0)    # 0% duty cycle to turn off the buzzer

# Play a simple sequence of tones
play_tone(440, 500)  # A4 note
time.sleep_ms(250)
play_tone(523, 500)  # C5 note
time.sleep_ms(250)
play_tone(659, 500)  # E5 note
time.sleep_ms(250)

# Turn off the buzzer
buzzer.deinit()
