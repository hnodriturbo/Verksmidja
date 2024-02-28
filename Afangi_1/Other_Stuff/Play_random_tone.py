
# Fallið sem spilar random tón úr tones listanum
def play_random_tone():
    tone = random.choice(tones)
    buzzer.freq(tone)
    buzzer.duty_u16(32768) # 50% duty cycle
    sleep_ms(2000)
    buzzer.duty_u16(0) # Turn off the buzzer

while True:
    if takki_1.value() == 1:
        play_random_tone()
        while takki_1.value() == 1:
            sleep_ms(10)
    sleep_ms(10)

    
#while True:
#    if takki_1.value() == 1:
#        speaker.value(1)
#        sleep_ms(100)
#        speaker.value(0)
#    sleep_ms(10)