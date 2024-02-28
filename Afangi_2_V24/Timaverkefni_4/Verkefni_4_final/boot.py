# boot.py

import esp
import gc
esp.osdebug(None)
# 
# import webrepl
# webrepl.start() 
# wifi_enabled = True  # Set to False to disable Wi-Fi connection attempts
# 
# if wifi_enabled:
#     from network_files.connect_network import connect_to_wifi, find_open_network_and_connect
#     if not connect_to_wifi():
#         print('Failed to connect to home network. Checking for open networks...')
#         if not find_open_network_and_connect():
#             print('No open networks available or failed to connect.')
# else:
#     print('Wi-Fi connection attempts are disabled.')
# 
# 
# # I used chatGPT to help me set the time from the connected network it connects to
# from set_time.set_time import set_time_from_ntp
# set_time_from_ntp()

gc.collect()
