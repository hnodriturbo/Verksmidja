import ntptime
import time
import machine


# Function to sync time with NTP
def sync_time():
    try:
        ntptime.settime()  # Sync with NTP server
        print("Time synchronized")
    except:
        print("Error synchronizing time")


# Convert the time to readable format
def get_time():
    rtc = machine.RTC()
    current_time = (
        rtc.datetime()
    )  # Get the time in (year, month, day, hour, minute, second) format
    print(
        f"Current time: {current_time[0]}-{current_time[1]}-{current_time[2]} {current_time[4]}:{current_time[5]}:{current_time[6]}"
    )


# Sync and print time
sync_time()
get_time()

# Optionally keep printing the current time every second
while True:
    get_time()
    time.sleep(1)
