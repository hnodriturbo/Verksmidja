import network
import time


def connect_to_wifi():
    # My internet at home
    home_ssid = 'Hringdu-2.4G-3kXq'  # Home 2.4 GHz SSID
    home_password = 'Faqbf39h'  # Home Wi-Fi password

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Attempting to connect to home network...')
        wlan.connect(home_ssid, home_password)
        for _ in range(10):  # Timeout after 10 attempts
            if wlan.isconnected():
                print('Connected to home network.')
                return True
            time.sleep(1)
    else:
        print('Already connected to a network.')
        return True

    return False

def find_open_network_and_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    for ssid, _, _, _, authmode, _ in networks:
        if authmode == 0:  # Authmode 0 indicates an open network
            print(f'Attempting to connect to open network: {ssid.decode()}')
            wlan.connect(ssid.decode())
            for _ in range(10):  # Timeout after 10 attempts
                if wlan.isconnected():
                    print('Connected to open network:', ssid.decode())
                    return True
                time.sleep(1)
            break  # Stop after trying the first open network found

    print('No open networks found.')
    return False

