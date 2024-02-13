# Tímaverkefni 1

- 10% af heildareinkunn
- Einstaklingsverkefni.
- Settu upp verklega.
- Passaðu að þú getir útskýrt fyrir kennara allan kóða sem þú skrifar.

## 1. NeoPixel (20%)

Notaðu NeoPixel hringinn sem fylgir með í ESP32 settinu þínu.

Tengingar (tengja IN megin):

NeoPixel | ESP32-S3
--- | ---
S | Pinninn sem á að stjórna NeoPixel
V | 3.3V
G | GND

Dæmi um kóða:
```python
from machine import Pin
from neopixel import NeoPixel

# búið til nýtt tilvik af NeoPixel klasanum, hringurinn
# er tengdur við pinna 10 og hefur átta perur
neo = NeoPixel(Pin(10), 8)

# litir stilltir með lista [RAUTT, GRÆNT, BLÁTT] þar sem
# hver litur getur tekið gildið frá 0 til og með 255
neo.fill([255, 0, 0]) # Allar perurnar fá sama litinn
neo.write() # Kallað á write til að senda litinn á hringinn

# Einnig hægt að stilla hverja peru sérstaklega
neo[0] = [0, 127, 127]
neo[1] = [63, 63, 63]
neo.write()
```

### Verkefnið

1. Láttu allar lýsa með sama lit í 2 sekúndur og skiptu svo um lit á öllum og láttu lýsa í 2 sekúndur og endurtaka.
1. Láttu lit ganga í hring (ein pera í einu).
1. Skiptu um átt.
1. Láttu peru 0, 2, 4 og 6 fá ákveðinn lit, láttu svo hinar perurnar fá annan lit og láttu svo litina víxlast eins og lögguljós. 

## 2. LCD 16x2 (10%)

Notað LCD skjáinn sem fylgir með í ESP32 settinu þínu.

Tengingar:

LCD | ESP32-S3
--- | ---
GND (1) | GND
VCC (2) | :warning: 5V 
SDA (3) | Pinni til að stjórna skjánum
SCL (4) | Pinni til að stjórna skjánum

Þú þarft að sækja klasasöfnin **I2C_LCD.py** og **LCD_API.py** og setja þau inn á ESP-inn þinn, þú finnur klasasöfnin [hér](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_ESP32_S3/tree/main/Python/Python_Libraries):

```python
from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd

# Skjárinn nota I2C tengingu til að tala við ESP
i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)

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

# Færi bendilinn í staf nr. 0 og línu nr. 0
lcd.move_to(0, 0)
lcd.putstr("Hallo")
# Færi bendilinn í staf nr. 0 og línu nr. 1
lcd.move_to(0, 1)
lcd.putstr("Heimur")

# Skoðaðu skrána LCD_API.py til að kynna þér önnur föll sem 
# hægt er að nota með LCD skjánum
```

### Verkefnið

Forritaðu teljara sem LCD skjárinn birtir. Teljarinn á að byrja að telja frá núll og upp í 30 og þegar hann er kominn upp í 30 á hann að telja niður í 0. Þetta á svo að endurtaka að eilífu. Hver tala á að birtast á skjánum í eina sekúndu.

## 3. Teningur (10%)

Bættu núna takka við rásina úr liðnum hér fyrir ofan (2) og forritaðu svo tening. Þegar ýtt er í takkann á að koma upp tala sem valin er af handahófi (e. random). Talan á svo að standa á LCD skjánum þar til ýtt er aftur á takkan og þá á ný tala að birtast.

Bjargir: [Takkar](https://github.com/VESM2VT/ESP32/blob/main/kennsluefni/digital.md#takkar---pull-up-og-pull-down), [Debounce](https://github.com/VESM2VT/ESP32/blob/main/kennsluefni/digital.md#debounce)

## 4. Skeiðklukka (20%)

Forritaðu skeiðklukku sem byrjar að telja frá núll þegar ýtt er á takka. Ef ýtt er aftur á sama takka stöðvast talningin og sú tala sem talningin var komin upp í helst á skjánum. Ef ýtt er aftur á sama takka heldur talningin áfram. Hafðu svo annan takka sem virkar þannig að þegar ýtt er á hann þá núllast talningin.

Bjargir: [Timer](https://docs.micropython.org/en/latest/esp32/quickref.html#timers) og nánar [hér](https://docs.micropython.org/en/latest/library/machine.Timer.html)

## 5. BOBA (40%)

1. Skrifaðu forrit fyrir niðurteljara sem virkar með LCD og NeoPixel. Niðurteljarinn á að byrja á 60 sekúndum og telja niður í núll. 
1. Tengdu þrjá víra við ESP-inn og í GND og forritaðu þá sem takka. Til að stöðva teljara þarf að klippa ákveðinn lit af vír, var það rauði eða kannski blái vírinn?
1. Ef klippt er á rangan vír þá verður niðutalningin tvöfalt hraðari. 

## Námsmat og skil
- Yfirferð og námsmat á sér stað í tíma. 
- Fyrir hvern lið; gefið er heilt fyrir fullnægjandi lausn, hálft ef lausn er ábótavant, ekkert ef lausn er stórlega ábótavant eða vantar. 
- Skilaðu á Innu öllum kóðalausnum.
