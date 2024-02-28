# This is time/set_time.py

def set_time_from_ntp():
    import ntptime
    try:
        timeString = ntptime.settime()  # This sets the system time from NTP
        print(f"Time set from NTP. Time is: {timeString}")
    except Exception as e:
        print('Failed to set time from NTP:', str(e))
