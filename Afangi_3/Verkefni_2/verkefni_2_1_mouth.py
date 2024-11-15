from machine import Pin
from lib.servo.servo import Servo
import time

# Define min and max angles for the servo movement
MIN_ANGLE = 20  # Mouth closed position
MAX_ANGLE = 70  # Mouth fully open position

# Define speed and movement step size
SPEED = 0.2  # Time delay between each movement (in seconds)
MOVEMENT_STEP = 5  # Step size for each movement in degrees

# Initialize the Servo on pin 19
print("Initializing Servo on pin 19...")
servo = Servo(Pin(8))
print("Servo initialized.")

# Define a function to move the servo to a specified angle and print feedback
def move_servo(degrees):
    """
    Move the servo to the specified angle.
    :param degrees: The angle to move the servo to (in degrees).
    """
    print(f"Moving Servo to {degrees} degrees...")
    servo.write_angle(degrees=degrees)

# Main function to continuously move the servo between min and max angles
def continuous_movement():
    """
    Continuously move the servo between MIN_ANGLE and MAX_ANGLE.
    """
    degrees = MIN_ANGLE  # Start at the minimum position
    movement_step = MOVEMENT_STEP  # Initial movement step

    print("Starting continuous servo movement...")

    while True:
        # Move the servo to the current angle
        move_servo(degrees)
        time.sleep(SPEED)  # Control delay with SPEED

        # Update the angle for the next movement
        degrees += movement_step

        # Reverse the direction if limits are reached
        if degrees >= MAX_ANGLE or degrees <= MIN_ANGLE:
            movement_step = -movement_step  # Reverse the direction

# Start the continuous movement
continuous_movement()
