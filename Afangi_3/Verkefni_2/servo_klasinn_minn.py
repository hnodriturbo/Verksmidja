import asyncio  # Using asyncio as requested
from machine import Pin
from lib.servo.servo import Servo  # Adjust path if necessary

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
        
    async def move_single_step_and_reverse_direction(self):
        """
        Moves the servo by a single step and reverses direction at the set limits.
        """
        print(f"Moving Servo {self.number} to {self.angle} degrees")
        self.servo.write_angle(degrees=self.angle)
        await asyncio.sleep(self.delay)

        # Update angle based on the current direction
        self.angle += self.step * self.direction

        # Reverse direction if the servo reaches its min or max angle
        if self.angle >= self.max_angle or self.angle <= self.min_angle:
            self.direction = -self.direction  # Reverse direction