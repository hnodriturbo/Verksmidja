from machine import Pin
from lib.servo.servo import Servo  # Import the Servo class from klasar/servo.py
import time

# Define the minimum and maximum angles
MIN_ANGLE = 20  # Closed
MAX_ANGLE = 70  # Fully open

# Set the speed of the movement (seconds between each step)
speed = 0.2  # Lower value = faster movement

# Initialize the Servo on pin 15
print("Initializing Servo on pin 15...")
servo = Servo(Pin(1))
print("Servo initialized.")

# Define a function to move the servo and print feedback
def move_servo(angle):
    print(f"Attempting to move servo to {angle} degrees...")
    servo.write_angle(degrees=angle)
    print(f"Servo successfully moved to {angle} degrees.")

# Continuously move the servo between MIN_ANGLE and MAX_ANGLE
try:
    angle = MIN_ANGLE  # Start at the minimum position
    movement = 5  # Step size for each movement

    print("Starting continuous servo movement...")
    while True:
        move_servo(angle)
        time.sleep(speed)  # Use the speed variable to control delay

        # Update angle for the next move
        angle += movement
        
        # Reverse direction when reaching limits
        if angle >= MAX_ANGLE or angle <= MIN_ANGLE:
            movement = -movement  # Reverse the direction

except KeyboardInterrupt:
    print("Servo control ended.")

