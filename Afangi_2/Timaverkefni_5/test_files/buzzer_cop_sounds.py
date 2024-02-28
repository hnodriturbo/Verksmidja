from machine import Pin, PWM
import time

# Initialize PWM for the buzzer with an initial frequency
buzzer_pin = 35  # Adjust based on your ESP32 board's capabilities
buzzer = PWM(Pin(buzzer_pin), freq=1000, duty=512)  # Initial frequency and duty

def change_tone(frequency):
    buzzer.freq(frequency)  # Change the frequency to alter the tone

def sound_buzzer(frequency, duration_ms=350):
    change_tone(frequency)  # Update the buzzer to the desired frequency
    time.sleep_ms(duration_ms)  # Keep the tone for the specified duration

# Keep the PWM active and avoid deinitializing it unnecessarily
try:
    #C4 = 262, E4 = 330 
    tones = [392, 523]  # Example tones in Hz (G4, C5) 
    print("starting while loop")
    while True:
        for tone in tones:
            sound_buzzer(tone)  # Play each tone
            print("playing a tone")
            time.sleep(0.1)  # Wait a bit before playing the next tone
finally:
    buzzer.deinit()  # Deinitialize the PWM when done to clean up

