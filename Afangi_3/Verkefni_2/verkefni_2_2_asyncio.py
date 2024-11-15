import asyncio  # Using asyncio as requested
from machine import Pin
from lib.servo.servo import Servo  # Adjust path if necessary

########################################################################################


# Here I created a class for each servo to create. Here I can use any pin number and give
# the servo a number or a name even to use it's instance to use asynchronous movements.
class ServoInstance:
    # Initialize each servo on the specified pin with a unique identifier
    def __init__(self, pin, number):
        self.number = number
        self.servo = Servo(Pin(pin))
        print(f"Servo {self.number} initialized on Pin {pin}.")

    async def move_single_step(self, angle, delay):
        """
        Moves the servo to a specified angle with a delay.
        """
        print(f"Moving Servo {self.number} to {angle} degrees")
        self.servo.write_angle(degrees=angle)
        await asyncio.sleep(delay)

########################################################################################

# Main function to create servo instances and control their movement
async def different_directions():
    # Create two servo instances on pins 12 and 13
    servo1 = ServoInstance(pin=12, number=1)
    servo2 = ServoInstance(pin=13, number=2)

    # Set initial positions for each servo within the valid range
    angle1, angle2 = 0, 180  # Servo 1 starts at 0, Servo 2 starts at 180
    step = 20                # Angle step size for each movement
    delay = 1                # Delay time between each movement step
    direction1, direction2 = 1, -1  # Initial directions (1 = forward, -1 = reverse)

    while True:
        print("Running movement cycle...")

        # Move each servo by one step in its direction
        await asyncio.gather(
            servo1.move_single_step(angle1, delay),
            servo2.move_single_step(angle2, delay)
        )

        # Update angles based on direction for each servo
        angle1 += step * direction1
        angle2 += step * direction2

        # Reverse direction if each servo reaches its min or max angle
        if angle1 >= 180 or angle1 <= 0:
            direction1 = -direction1  # Reverse direction for servo1
        if angle2 >= 180 or angle2 <= 0:
            direction2 = -direction2  # Reverse direction for servo2

########################################################################################

# Main function to create servo instances and control their movement in sync
async def same_direction():
    # Create two servo instances on pins 12 and 13
    servo1 = ServoInstance(pin=12, number=1)
    servo2 = ServoInstance(pin=13, number=2)

    # Set initial position and direction for both servos
    angle = 0      # Both servos start at 0 degrees
    delay = 0.1      # Delay time between each movement step
    direction = 1  # Initial direction (1 = forward, -1 = reverse)
    step = 5      # Angle degrees step size for each movement

    while True:
        print("Running synchronized movement cycle...")

        # Move both servos by one step in the same direction
        await asyncio.gather(
            servo1.move_single_step(angle, delay),
            servo2.move_single_step(angle, delay)
        )

        # Update angle based on direction
        angle += step * direction

        # Reverse direction if either servo reaches its min or max angle
        if angle >= 180 or angle <= 0:
            direction = -direction  # Reverse direction for both servos


# Run the asyncio event
# asyncio.run(different_directions())

# Run the asyncio event
asyncio.run(same_direction())

