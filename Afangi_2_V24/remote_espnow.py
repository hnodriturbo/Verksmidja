# Kóðinn á ESP-inn sem sendir skilaboð
from network import WLAN, STA_IF
from espnow import ESPNow
from time import sleep_ms

# Virkja þráðlausa netið
sta = WLAN(STA_IF)
sta.active(True)

sendir = ESPNow()
sendir.active(True)
hinn_esp_inn = BREYTTU_MÉR   # MAC address-an á hinum ESP-inum (bílnum)
sendir.add_peer(hinn_esp_inn)

teljari = 0

while True:
    # skilaboðin eru alltaf send sem strengur (eða bytestring) en við getum notum streng í þessum áfanga
    skilabod = f"{teljari} hallo"
    sendir.send(hinn_esp_inn, skilabod, True)
    teljari += 1
    sleep_ms(500)
  