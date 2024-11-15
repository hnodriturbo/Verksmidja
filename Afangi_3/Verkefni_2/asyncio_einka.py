import uasyncio as asyncio
from machine import Pin
from lib.servo.servo import Servo

class ServoMotor:
    def __init__(self, pin, name):
        print(f"Initializing {name} on Pin {pin}...")
        self.motor = Servo(Pin(pin))
        self.name = name
        print(f"{name} initialized successfully.")

    async def move(self, start_angle, end_angle, delay=0.5):
        angle = start_angle
        step = 5
        while True:
            print(f"Moving {self.name} to {angle} degrees")
            self.motor.write_angle(degrees=angle)
            await asyncio.sleep(delay)

            # Reverse direction at limits
            angle += step
            if angle >= end_angle or angle <= start_angle:
                step = -step  # Reverse direction

# Main asyncio function
async def main():
    motor1 = ServoMotor(12, "Motor 1")
    motor2 = ServoMotor(13, "Motor 2")
    
    await asyncio.gather(
        motor1.move(20, 80),
        motor2.move(30, 90)
    )

# Run the asyncio event loop
asyncio.run(main())
