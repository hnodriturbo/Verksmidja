import urequests
import time
from machine import Pin, PWM
from lib.servo.servo import Servo  # Adjust path if necessary

BASE_URL = "http://127.0.0.1:5000"  # Replace with your Flask server IP address

# GPIO setup for LED and servo controls
led_pins = {
    "LED1": {"r": Pin(7, Pin.OUT), "g": Pin(5, Pin.OUT), "b": Pin(6, Pin.OUT)},
    "LED2": {"r": Pin(11, Pin.OUT), "g": Pin(10, Pin.OUT), "b": Pin(9, Pin.OUT)}
}
servo1 = Servo(Pin(12))
servo2 = Servo(Pin(13))

# Initialize PWM for LEDs
led_pwm = {
    "LED1": {color: PWM(pin, freq=1000) for color, pin in led_pins["LED1"].items()},
    "LED2": {color: PWM(pin, freq=1000) for color, pin in led_pins["LED2"].items()}
}

# Function to set LED color
def set_color(led, r, g, b):
    led_pwm[led]["r"].duty(r)
    led_pwm[led]["g"].duty(g)
    led_pwm[led]["b"].duty(b)

# Check if the ESP32 can reach the server
def check_server_connection():
    try:
        response = urequests.get(f"{BASE_URL}/api/get_commands")
        response.close()
        print("[DEBUG] Server connection successful.")
        return True
    except Exception as e:
        print("Initial server connection failed:", e)
        return False

# Function to fetch and process commands from the backend
def fetch_and_process_commands():
    try:
        print("[DEBUG] Fetching commands from backend...")
        response = urequests.get(f"{BASE_URL}/api/get_commands")
        commands = response.json()
        response.close()
        print("[DEBUG] Commands received:", commands)
        
        # Update LEDs based on command
        for led in ["LED1", "LED2"]:
            if commands[led]["action"] == "on":
                set_color(led, *commands[led]["color"])
                print(f"[DEBUG] Set {led} color to {commands[led]['color']}")
            else:
                set_color(led, 0, 0, 0)  # Turn off LED
                print(f"[DEBUG] Turned off {led}")
        
        # Update servos based on command
        for servo_name, servo in [("servo1", servo1), ("servo2", servo2)]:
            if commands[servo_name]["action"] == "move":
                start = commands[servo_name]["start_angle"]
                end = commands[servo_name]["end_angle"]
                print(f"[DEBUG] Moving {servo_name} from {start} to {end}")
                # Perform movement
                for angle in range(start, end + 1, 5):
                    servo.write_angle(angle)
                    time.sleep(0.05)
                for angle in range(end, start - 1, -5):
                    servo.write_angle(angle)
                    time.sleep(0.05)
            else:
                print(f"[DEBUG] No movement command for {servo_name}")
                    
    except Exception as e:
        print("Error in fetch_and_process_commands:", e)
        time.sleep(5)  # Wait before retrying

# Main loop to fetch commands periodically
def main():