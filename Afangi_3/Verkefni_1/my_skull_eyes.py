from machine import Pin, PWM
import time
import random

# Set this to True for both LEDs to show the same color, or False for independent colors
same_color = True  # Set to False if you want each LED to show different colors

# Configuration settings for smooth color transitions
step_size = 1        # Smaller step size for smoother transition
delay = 0.01         # Delay between steps for smooth transitions
blink_delay = 0.2    # Delay for blinking effect

# Define mostly red color ranges for each LED
color_ranges = {
    "LED1": {
        "r": (800, 1023),   # High range for red intensity on LED 1
        "g": (0, 100),      # Lower range for green intensity on LED 1
        "b": (0, 100)       # Lower range for blue intensity on LED 1
    },
    "LED2": {
        "r": (800, 1023),   # High range for red intensity on LED 2
        "g": (0, 100),      # Lower range for green intensity on LED 2
        "b": (0, 100)       # Lower range for blue intensity on LED 2
    }
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
    # Turn off the LED by setting duty cycle to 0
    set_color(led, 0, 0, 0)
    time.sleep(blink_delay)  # Short delay for blink effect
    # Restore the LED to the specified color
    set_color(led, r, g, b)

# Function to generate random color within defined ranges
def random_color(led):
    r = random.randint(*color_ranges[led]["r"])
    g = random.randint(*color_ranges[led]["g"])
    b = random.randint(*color_ranges[led]["b"])
    return r, g, b

# Function for smooth color transitions with optional synchronization and blinking
def smooth_transition():
    # Initialize current and target colors for each LED
    current_colors = {
        "LED1": random_color("LED1"),
        "LED2": random_color("LED2") if not same_color else None
    }
    target_colors = {
        "LED1": random_color("LED1"),
        "LED2": random_color("LED2") if not same_color else None
    }

    # Start smooth transitions
    while True:
        for led in ["LED1", "LED2"]:
            if same_color and led == "LED2":
                current_colors[led] = current_colors["LED1"]
                target_colors[led] = target_colors["LED1"]
            else:
                # Check if current color matches the target; if so, pick a new random target
                if current_colors[led] == target_colors[led]:
                    # Perform blink effect before changing to a new target color
                    blink(led, *current_colors[led])

                    # Set a new target color
                    target_colors[led] = random_color(led)

            # Update each color component (r, g, b) towards its target for a smooth transition
            new_colors = []
            for current, target in zip(current_colors[led], target_colors[led]):
                if current < target:
                    current = min(current + step_size, target)
                elif current > target:
                    current = max(current - step_size, target)
                new_colors.append(current)

            # Update current color values and set the new color on the LED
            current_colors[led] = tuple(new_colors)
            set_color(led, *current_colors[led])

        # Delay for smooth transitions
        time.sleep(delay)

# Start the smooth color transitions
smooth_transition()
