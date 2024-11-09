import asyncio 
from machine import Pin
from lib.servo.servo import Servo 

########################################################################################


# My Servo class to create instances with as many options as possible. This way
# I can control the instance much better and they also run better asynchrounisly
class ServoInstance:
    def __init__(self, pin, number, min_angle, max_angle, step, delay, direction=True):
        # Initialize each servo on the specified pin with a unique identifier and movement settings
        self.number = number
        self.servo = Servo(Pin(pin))
        # Min angle and max angle for the servo to go to
        self.min_angle = min_angle
        self.max_angle = max_angle
        # Steps in degrees
        self.step = step
        # Delay between steps
        self.delay = delay
        # If direction is true start at min_angle, else start at max_angle (to make them go in seperate directions)
        self.angle = min_angle if direction else max_angle
        # Set direction to 1 if direction=True else direction -1
        self.direction = 1 if direction else -1  
        print(f"Servo {self.number} initialized on Pin {pin} with range {self.min_angle}-{self.max_angle}.")

    async def move_single_step(self):
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

########################################################################################

# Main function to create servo instances and control their movement
async def alternate_movements():
    # Create two servo instances with unique settings
    servo1 = ServoInstance(pin=12, number=1, min_angle=30, max_angle=120, step=1, delay=0.01, direction=True)
    servo2 = ServoInstance(pin=13, number=2, min_angle=60, max_angle=150, step=1, delay=0.01, direction=False)

    while True:
        print("Running movement cycle...")

        # Move each servo by one step asynchronously
        await asyncio.gather(
            servo1.move_single_step(),
            servo2.move_single_step()
        )

# Run the asyncio event loop
asyncio.run(alternate_movements())

