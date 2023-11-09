# ----------- Sækjum auka forritasöfn -----------
from machine import Pin, PWM, ADC
# Pin er með grunnstilingar pinna
# PWM gerir pinnum kleyft að skrifa hliðrænt (e. analog)
# ADC gerir vissum pinnum kleyft að lesa hliðrænt.
from time import sleep_ms
import random

# Set upp perurnar í python lista aðallega svo ég geti random valið peru til að kvikna
#leds = [Pin(9, Pin.OUT), Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(46, Pin.OUT)]
# Set upp takkana svona inn í python lista svo ég geti accessað þá út frá index
#buttons = [Pin(15, Pin.IN, Pin.PULL_DOWN), Pin(16, Pin.IN, Pin.PULL_DOWN), Pin(17, Pin.IN, Pin.PULL_DOWN), Pin(18, Pin.IN, Pin.PULL_DOWN)]


# LED perurnar
rautt = Pin(9, Pin.OUT) # Pinni 9 skilgreindur sem úttakspinni (stafrænn)
graent = Pin(10, Pin.OUT) # Pinni 10 skilgr. sem úttakspinni (stafrænn)
blatt = Pin(11, Pin.OUT) # Pinni 11 skilgr. sem úttakspinni (stafrænn)
gult = Pin(46, Pin.OUT)

# Takkarnir
takki_1 = Pin(15, Pin.IN,Pin.PULL_DOWN)
takki_2 = Pin(16, Pin.IN,Pin.PULL_DOWN)
takki_3 = Pin(17, Pin.IN,Pin.PULL_DOWN)
takki_4 = Pin(18, Pin.IN,Pin.PULL_DOWN)

# Speakerinn - Passive
speaker = Pin(6, Pin.OUT) 

# Speakerinn - Passive PWM
buzzer = PWM(speaker)

#led_state = False # LED starts in the off state
#last_button_state = False # Last known state of the button


# List of LEDs and buttons for easier management
leds = [gult, rautt, graent, blatt]
        # 0		1		2		3
buttons = [takki_1, takki_2, takki_3, takki_4]
            # 0			1		2		3

# Tónar fyrir speakerinn - notaði þetta til að æfa mig
tones = [262, 330, 392, 494]

# Vinnings og tap tónar - niður og upp
losing_tones = [440, 349, 294, 220]  # A4, F4, D4, A3
winning_tones = [523, 659, 784, 1047]  # C5, E5, G5, C6

# Stilli hávaðann á passive buzzer á 0
buzzer.duty_u16(0)

# Fall sem spilar alla tóna í listanum i 200ms með 100ms millibili (gert til að spila bæði tap og vinnings hljóðin)
def play_tone_sequence(sequence):
    for tone in sequence:
        buzzer.freq(tone) # Stilli frequenzy buzzer á hvern tón í listanum
        buzzer.duty_u16(32768) # 50% duty cycle
        sleep_ms(200) # Spila tóninn í 200ms
        buzzer.duty_u16(0) # Slekk á buzzer
        sleep_ms(100) # Stutt pása milli tóna
        # repeat repeat repeat repeat - for lúppan spilar alla tónana i listanum
        
# Gerði þetta þegar ég var bæta við að ljós lýsast upp þegar leikmaður vinnur
def play_tone(tone):
    buzzer.freq(tone)
    buzzer.duty_u16(32768)
    sleep_ms(200)
    buzzer.duty_u16(0)
        
# Fall sem bíður i tvær sekóntur - eftir langa hugsun og pælingar og prófanir varð þetta niðurstaðan
def wait_for_input(led_index, countdown_time):
    while countdown_time > 0:
        if buttons[led_index].value():
            return True
        sleep_ms(10) # Bíða aðeins áður en athugað er aftur hvort að ýtt hafi verið á takkann
        countdown_time -= 10
    return False # Ef fallið nær að keyra ms með countdown -= 10 í hvert skipti niður í 0 þá tapar leikmaður



def win():
    for x in range(4):
        for i in range(len(leds)):
            leds[i].value(1) # Kveiki á peru
            play_tone(winning_tones[i]) # Spilar tón eftir tón út frá index í 200ms
            sleep_ms(100) # 0.1 sek bið á milli
            leds[i].value(0) # Slekk á perunni
            
def turn_off_leds():
    for led in leds:
        led.value(0)
        
def turn_on_leds():
    for led in leds:
        led.value(1)
        
def blink_leds(sleep):
    turn_on_leds()
    sleep
    turn_off_leds()
    sleep
        
# Fallið sem spilar leikinn
def play_game():
    while True:
        turn_off_leds()
        # Random vel eina led peruna til að kvikna
        led_index = random.randint(0,3) # 0, 1, 2, 3 er index led listans
        # Kveiki a einni random peru
        leds[led_index].value(1)
        
        # Bíð í tvær sekóntur eftir viðbragði leikmanns
        player_correct = wait_for_input(led_index, 2000)
        
        if player_correct:
            win()
        else:
            play_tone_sequence(losing_tones)
            turn_off_leds()
            
        sleep_ms(5000) # Bíð 5 sekóntur aður en nýr leikur hefst
        
        turn_off_leds()
        
        
# Og keyra leikinn !!!!
play_game()

