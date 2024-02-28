# boot.py
import esp
esp.osdebug(None)  # Disable vendor OS debugging messages

import gc
# import webrepl

# webrepl.start()  # Starts WebREPL with the previously set password
# 
# try:
#     # Attempt to connect to Wi-Fi
#     import connect_network
#     connect_network.connect_to_wifi()
# except Exception as e:
#     print("Could not connect to Wi-Fi:", str(e))

gc.collect()  # Run garbage collection to free up memory