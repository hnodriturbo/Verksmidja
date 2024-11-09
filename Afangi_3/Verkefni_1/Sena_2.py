import network
import ntptime
from machine import Pin, PWM, Timer, RTC
import time

# Class for RGB LED control
class RGBLED:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red = PWM(Pin(red_pin), freq=1000)
        self.green = PWM(Pin(green_pin), freq=1000)
        self.blue = PWM(Pin(blue_pin), freq=1000)

    def set_color(self, r, g, b):
        self.red.duty(r)
        self.green.duty(g)
        self.blue.duty(b)

    def blink_leds(self, duration_ms):
        start_time = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
            for color in [(1023, 0, 0), (0, 1023, 0), (0, 0, 1023)]:
                self.set_color(*color)
                time.sleep_ms(500)
        self.set_color(0, 0, 0)

# Class for controlling the Servo
class ServoMotor:
    def __init__(self, pin):
        self.servo = PWM(Pin(pin), freq=50)

    def move(self, angle):
        duty = int((angle / 180) * 1023)
        self.servo.duty(duty)

    def open_mouth(self):
        self.move(80)

    def close_mouth(self):
        self.move(20)

    def slight_open(self):
        self.move(50)

    def continuous_movement(self, start_angle, end_angle, step=5, speed=0.2):
        angle = start_angle
        direction = step
        while True:
            self.move(angle)
            time.sleep(speed)
            angle += direction
            if angle >= end_angle or angle <= start_angle:
                direction = -direction

# Class for time synchronization
class TimeSync:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.rtc = RTC()

    def connect_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            wlan.connect(self.ssid, self.password)
            while not wlan.isconnected():
                pass
        print("Connected:", wlan.ifconfig())

    def sync_time(self):
        try:
            ntptime.settime()
            print("Time synchronized")
        except OSError as e:
            print(f"Error syncing time: {e}")

    def get_time(self):
        _, _, _, hour, minute, second, _, _ = self.rtc.datetime()
        return hour, minute, second

# Main class to control the scene
class SkullScene:
    def __init__(self):
        self.rgb_led = RGBLED(15, 16, 17)
        self.servo_motor = ServoMotor(13)
        self.time_sync = TimeSync("SSID", "password")

    def start_scene(self):
        self.time_sync.connect_wifi()
        self.time_sync.sync_time()
        self.start_timed_scene()

    def start_timed_scene(self):
        timer = Timer(-1)
        timer.init(period=10000, mode=Timer.PERIODIC, callback=lambda t: self.run_mood_scene())

    def run_mood_scene(self):
        print("Mood: Happy")
        self.rgb_led.set_color(0, 1023, 0)
        self.servo_motor.open_mouth()
        time.sleep(2)

        print("Mood: Sad")
        self.rgb_led.set_color(0, 0, 1023)
        self.servo_motor.slight_open()
        time.sleep(2)

        print("Mood: Angry")
        self.rgb_led.set_color(1023, 0, 0)
        self.servo_motor.open_mouth()
        time.sleep(2)

        self.rgb_led.blink_leds(5000)
        self.servo_motor.close_mouth()

# Run the scene
skull_scene = SkullScene()
skull_scene.start_scene()
