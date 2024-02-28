import time

# Get the current time as a tuple
current_time_tuple = time.localtime()  # Returns (year, month, day, hour, minute, second, weekday, yearday)

# Format the time manually
current_timestamp = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*current_time_tuple[0:6])

print(current_timestamp)
