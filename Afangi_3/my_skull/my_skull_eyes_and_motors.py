import asyncio  # Only asyncio is imported
import random
import time
from machine import Pin, PWM
from lib.servo.servo import Servo  # Adjust path if necessary

# Set this to True for both LEDs to show the same color, or False for independent colors
same_color = True  # Set to False if you want each LED to show different colors

# Configuration settings for smooth color transitions
step_size = 1       # Smaller step size for smoother transition
delay = 0.01        # Delay between steps for smooth transitions
blink_delay = 0.2   # Delay for blinking effect

# Define mostly red color ranges for each LED
color_ranges = {
    "LED1": {"r": (800, 1023), "g": (0, 100), "b": (0, 100)},
    "LED2": {"r": (800, 1023), "g": (0, 100), "b": (0, 100)}
}

# Define RGB pin connections for each LED
led_pins = {
    "LED1": {"r": Pin(7, Pin.OUT), "g": Pin(5, Pin.OUT), "b": Pin(6, Pin.OUT)},
    "LED2": {"r": Pin(16, Pin.OUT), "g": Pin(17, Pin.OUT), "b": Pin(18, Pin.OUT)}
}

# Initialize PWM for each color channel
led_pwm = {
    "LED1": {color: PWM(pin, freq=1000) for color, pin in led_pins["LED1"].items()},
    "LED2": {color: PWM(pin, freq=1000) for color, pin in led_pins["LED2"].items()}
}

# Function to set color for a given LED
def set_color(led, r, g, b):
    led_pwm[led]["r"].duty(r)
    led_pwm[led]["g"].duty(g)
    led_pwm[led]["b"].duty(b)

# Function to blink the LED off and back to the given color
def blink(led, r, g, b):
    set_color(led, 0, 0, 0)  # Turn off the LED
    time.sleep(blink_delay)  # Short delay for blink effect
    set_color(led, r, g, b)  # Restore the LED to the specified color

# Function to generate random color within defined ranges
def random_color(led):
    r = random.randint(*color_ranges[led]["r"])
    g = random.randint(*color_ranges[led]["g"])
    b = random.randint(*color_ranges[led]["b"])
    return r, g, b

# Function for smooth color transitions with optional synchronization and blinking
async def smooth_transition():
    current_colors = {"LED1": random_color("LED1"), "LED2": random_color("LED2")}
    target_colors = {
        "LED1": random_color("LED1"),
        "LED2": random_color("LED1") if same_color else random_color("LED2")
    }

    while True:
        for led in ["LED1", "LED2"]:
            if current_colors[led] == target_colors[led]:
                blink(led, *current_colors[led])  # Blink before transitioning to a new color
                target_colors[led] = random_color("LED1") if same_color else random_color(led)

            new_colors = []
            for current, target in zip(current_colors[led], target_colors[led]):
                if current < target:
                    current = min(current + step_size, target)
                elif current > target:
                    current = max(current - step_size, target)
                new_colors.append(current)

            current_colors[led] = tuple(new_colors)
            set_color(led, *current_colors[led])

        await asyncio.sleep(delay)

########################################################################################

# Servo Control Class
class ServoInstance:
    def __init__(self, pin, number):
        # Initialize each servo on the specified pin with a unique identifier
        self.number = number
        self.servo = Servo(Pin(pin))
        print(f"Servo {self.number} initialized successfully on Pin {pin}.")

    async def move_parts_of_angle(self, start_angle, end_angle, delay, step):
        """
        Move the servo back and forth between start_angle and end_angle at a given speed,
        completing a full cycle before returning.
        """
        angle = start_angle
        moving_forward = True  # Track direction to know when a full cycle is complete

        while True:
            print(f"Moving Servo {self.number} to {angle} degrees")
            self.servo.write_angle(degrees=angle)
            await asyncio.sleep(delay)

            # Adjust angle based on direction
            if moving_forward:
                angle += step
                if angle >= end_angle:
                    angle = end_angle
                    moving_forward = False  # Start moving backward
            else:
                angle -= step
                if angle <= start_angle:
                    angle = start_angle
                    break  # End loop after reaching start_angle

# Main function to create servo instances and alternate fast and slow movements for full cycles
async def alternate_movements():
    # Create two instances of ServoInstance with pins 12 and 13
    servo1 = ServoInstance(pin=12, number=1)
    servo2 = ServoInstance(pin=13, number=2)

    while True:
        # Run both servos with a complete fast movement cycle
        print("Running fast movement...")
        await asyncio.gather(
            servo1.move_parts_of_angle(start_angle=0, end_angle=180, delay=0.01, step=1),
            servo2.move_parts_of_angle(start_angle=0, end_angle=180, delay=0.01, step=1)
        )

        # Run both servos with a complete slow movement cycle
        print("Running slow movement...")
        await asyncio.gather(
            servo1.move_parts_of_angle(start_angle=0, end_angle=180, delay=0.2, step=5),
            servo2.move_parts_of_angle(start_angle=0, end_angle=180, delay=0.2, step=5)
        )

# Main asyncio function to run both LED and motor control
async def main():
    # Run both LEDs and motors concurrently
    await asyncio.gather(
        smooth_transition(),
        alternate_movements()
    )

# Start the asyncio event loop
asyncio.run(main())
