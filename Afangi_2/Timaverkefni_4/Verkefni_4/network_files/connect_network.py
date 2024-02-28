import network

def connect_to_wifi():
    ssid = 'Hringdu-2.4G-3kXq'  # Your 2.4 GHz SSID
    password = 'Faqbf39h'  # Your Wi-Fi password

    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)  # Activate the interface

    if not wlan.isconnected():  # Check if already connected
        print('Connecting to network...')
        wlan.connect(ssid, password)  # Connect to the network
        while not wlan.isconnected():  # Wait until connected
            pass  # You can optionally add a timeout here

    print('Network config:', wlan.ifconfig())  # Print IP address, subnet mask, gateway, and DNS

# Call the function to connect to the Wi-Fi
connect_to_wifi()
