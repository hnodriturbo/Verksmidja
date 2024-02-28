import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='MyESP32', password='Hnodri')

print('Network created:', ap.ifconfig())
