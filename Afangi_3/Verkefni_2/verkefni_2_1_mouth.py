from machine import Pin
from lib.servo.servo import Servo
import time

# Ég er búinn finna út að munnurinn í mínu módeli er með þessi min og max angles
MIN_ANGLE = 20  # Closed
MAX_ANGLE = 70  # Fully open


# Bjó til hraða breytu þannig ég get stillt hversu hratt er á milli hverra 5 gráðna
speed = 0.2  # How long time between movements
movement = 5  # Step size for each movement

# Initialize the Servo on pin 15
print("Initializing Servo on pin 15...")
servo = Servo(Pin(15))
print("Servo initialized.")

# Define a function to move the servo and print feedback
def move_servo(angle):
    # Print for debugging
    print(f"Moving Servo to {angle} degrees...")
    servo.write_angle(degrees=angle)


    degrees = MIN_ANGLE  # Start at the minimum position
    
    print("Starting continuous servo movement...")
    
    while True:
        move_servo(degrees)
        time.sleep(speed)  # Use the speed variable to control delay

        # Update angle for the next move
        degrees += movement
        
        # Reverse direction when reaching limits
        if degrees >= MAX_ANGLE or degrees <= MIN_ANGLE:
            movement = -movement  # Reverse the direction


