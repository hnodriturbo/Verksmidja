from machine import Pin, PWM
from machine import SoftI2C
from I2C_LCD import I2cLcd
# Ég importa bara time í heild sinni og nota time.eitthvað á undan hverri skipun i staðinn
import time



# Stilli Ultrasonic sensorinn
echo = Pin(47, Pin.IN)
trig = Pin(48, Pin.OUT)

# Græja takkann
button = Pin(19, Pin.IN, Pin.PULL_UP)

# Þarf ekki perurnar né buzzer núna þannig skil það eftir hér

# Stilli inn perurnar
#led1 = Pin(11, Pin.OUT)
#led2 = Pin(12, Pin.OUT)
#led3 = Pin(13, Pin.OUT)

# Stilli inni passíva buzzerinn á pin 3 og duty 0
#buzzer = PWM(Pin(3), duty=0)

# Fallið sem mælir vegalengd i sentimetrum
def measure_distance():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    

    while not echo.value():
        pass
    start = time.ticks_us()

    while echo.value():
        pass
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    
    distance = (duration * 0.0343) / 2
    
    # Þessi leið er líka valid miðað við hvað ég les á netinu um þetta
    #trig.value(0)
    #time.sleep_us(2)
    #trig.value(1)
    #time.sleep_us(10)
    #trig.value(0)

    
    
    # Skila úr fallinu lengdina sem reiknuð hefur verið. Athugaðu að þessi kóði
    # er sá sem ég fékk úr sýnishorninu til að mæla vegalengdina en ég samsetti
    # hann hérna innan í fall sem mér þykir þægilegra
    return round(distance, 2) # Passa að fallið skilar bara 2 stöfum eftir kommu



# Stilli inn skjáinn og nota kóða frá sýnishorninu

# Skjárinn nota I2C tengingu til að tala við ESP
i2c = SoftI2C(scl=Pin(41), sda=Pin(21), freq=400000)

# Mörg tæki geta notað sömu tenginguna, 
# scan skilar lista af öllum tækjunum sem fundust
taekin = i2c.scan()

# Við erum bara með eitt tæki (skjáinn)
if len(taekin) == 0:
    print("Fann ekki skjáinn")
else:
    # búum til tilvik af skjánum, skjárinn 
    # hefur 2 línur og 16 stafi í hvorri línu
    lcd = I2cLcd(i2c, taekin[0], 2, 16)


# Set vistaða vegalengd sem ekkert til að búa hana til
saved_distance = None
# Fyrri staða takkans
previous_button_state = True

def display_measurement(distance, saved_distance):
    # Sýna vegalengdina með því að setja bendil skjásins á 0
    lcd.move_to(0, 0)
    lcd.putstr("Raun: " + str(distance) + " cm ")


while True:
    distance = measure_distance()
    
    # Sýna vegalengdina með því að setja bendil skjásins á 0
    lcd.move_to(0, 0)
    lcd.putstr("Raun: " + str(distance) + " cm ")

    # Nú þarf ég að höndla takka ýtinguna til að vista vegalengdina
    current_button_state = button.value()
    if current_button_state == 0 and previous_button_state == 1:
        saved_distance = distance
        
    # Sýna vistuðu vegalengdina
    lcd.move_to(0, 1)
    if saved_distance is not None:
        lcd.putstr("Geymt: " + str(saved_distance) + " cm")

    previous_button_state = current_button_state

    time.sleep(0.5)

