from machine import Pin, PWM
# Ég importa bara time í heild sinni og nota time.eitthvað á undan hverri skipun i staðinn
import time

# Stilli inn perurnar
led1 = Pin(11, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(13, Pin.OUT)

# Stilli inni passíva buzzerinn á pin 3 og duty 0
buzzer = PWM(Pin(3), duty=0)

# Stilli Ultrasonic sensorinn
echo = Pin(47, Pin.IN) # Pin(39, Pin.IN)
trig = Pin(48, Pin.OUT) # Pin(38, Pin.OUT)

# Fallið sem mælir vegalengd i sentimetrum
def measure_distance():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    # Þessi leið er líka valid miðað við hvað ég les á netinu um þetta
    #trig.value(0)
    #time.sleep_us(2)
    #trig.value(1)
    #time.sleep_us(10)
    #trig.value(0)

    while not echo.value():
        pass
    start = time.ticks_us()

    while echo.value():
        pass
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    
    distance = (duration * 0.0343) / 2
    
    # Skila úr fallinu lengdina sem reiknuð hefur verið. Athugaðu að þessi kóði
    # er sá sem ég fékk úr sýnishorninu til að mæla vegalengdina en ég samsetti
    # hann hérna innan í fall sem mér þykir þægilegra
    return distance

# Fallið sem updates status á perum og buzzer útfrá lengdinni sem er sett inn í fallið
def update_status(distance):
    if distance >= 100:
        led1.on()
        led2.on()
        led3.on()
        buzzer.duty(0)
    elif 80 <= distance < 100:
        led1.off()
        led2.on()
        led3.on()
        buzzer.duty(0)
    elif 60 <= distance < 80:
        led1.off()
        led2.off()
        led3.on()
        buzzer.duty(0)
    elif 40 <= distance < 60:
        led1.off()
        led2.off()
        led3.off()
        buzzer.duty(0)
    else:
        led1.off()
        led2.off()
        led3.off()
        buzzer.freq(440)  # Set buzzer frequency (stilli hvaða frequensy er valin (valdi bara einhverja))
        buzzer.duty(512)  # Kveiki á buzzer á 512 (hreinasti tónninn skilst mér)



# Bý til lúppu sem keyrir föllin og prentar út lengdina sem mælist
# og föllin kveikja á perunum í samræmi við verkefnið. ATH eg þurfti not öfugt on/off
# á perurnar svo það kæmi rétt út. Er ekki alveg viss afhverju það þurfti vera þannig.

while True:
    distance = measure_distance()
    update_status(distance)
    print(distance)
    time.sleep(0.5)

# Cleanup - Slökkva á buzzer
buzzer.deinit()
