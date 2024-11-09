import ntptime
import time
from machine import Pin, PWM


# Class for controlling RGB LEDs
class RGBLED:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red = PWM(Pin(red_pin), freq=1000)
        self.green = PWM(Pin(green_pin), freq=1000)
        self.blue = PWM(Pin(blue_pin), freq=1000)

    def set_color(self, r, g, b):
        self.red.duty(r)
        self.green.duty(g)
        self.blue.duty(b)

    def color_cycle(self):
        # Cycle through the colors
        self.set_color(1023, 0, 0)  # Red
        time.sleep(1)
        self.set_color(0, 1023, 0)  # Green
        time.sleep(1)
        self.set_color(0, 0, 1023)  # Blue
        time.sleep(1)


# Class for synchronizing time with NTP
class TimeSync:
    def __init__(self):
        self.rtc = None

    def sync_time(self):
        try:
            ntptime.settime()  # Sync with NTP server
            print("Time synchronized")
        except:
            print("Error synchronizing time")

    def get_time(self):
        rtc = machine.RTC()
        current_time = (
            rtc.datetime()
        )  # Get the time in (year, month, day, hour, minute, second) format
        print(
            f"Current time: {current_time[0]}-{current_time[1]}-{current_time[2]} {current_time[4]}:{current_time[5]}:{current_time[6]}"
        )
        return current_time


# Class for controlling a Servo/Motor (e.g., for the skull mouth)
class ServoMotor:
    def __init__(self, pin):
        self.servo = PWM(Pin(pin), freq=50)

    def move(self, angle):
        duty = int((angle / 180) * 1023)  # Adjust duty based on angle
        self.servo.duty(duty)

    def open_mouth(self):
        self.move(80)  # Open the mouth

    def close_mouth(self):
        self.move(20)  # Close the mouth


# Class to create the scene combining all components
class SkullScene:
    def __init__(self):
        self.rgb_led = RGBLED(15, 16, 17)  # Set your RGB LED pins
        self.servo_motor = ServoMotor(13)  # Set your Servo pin
        self.time_sync = TimeSync()

    def start_scene(self):
        # Sync time first
        self.time_sync.sync_time()

        # Start some scene logic
        for _ in range(3):  # Loop through a scene 3 times as an example
            self.rgb_led.color_cycle()  # Cycle RGB colors
            self.servo_motor.open_mouth()  # Open the mouth
            time.sleep(1)
            self.servo_motor.close_mouth()  # Close the mouth
            time.sleep(1)


# Main execution of my script and classes
if __name__ == "__main__":
    skull_scene = SkullScene()
    skull_scene.start_scene()
