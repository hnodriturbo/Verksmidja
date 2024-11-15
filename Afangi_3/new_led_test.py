import time
import random
from machine import Pin, PWM
import asyncio

# RGB LED Controller Class
class RGBController:
    def __init__(self, red_pin, green_pin, blue_pin):
        # Initialize PWM pins for each color to allow duty cycle control (0-1023)
        self.red = PWM(Pin(red_pin), freq=1000)
        self.green = PWM(Pin(green_pin), freq=1000)
        self.blue = PWM(Pin(blue_pin), freq=1000)
        self.blinking = True
        print(f"Initialized LED at red: {red_pin}, green: {green_pin}, blue: {blue_pin}")

    async def blink(self, interval=0.5):
        """
        Blink the LED colors in sequence.
        :param interval: Time delay between each color change.
        """
        while self.blinking:
            self.red.duty(1023)  # Full brightness (red on)
            self.green.duty(0)   # Green off
            self.blue.duty(0)    # Blue off
            await asyncio.sleep(interval)
            
            self.red.duty(0)     # Red off
            self.green.duty(1023)  # Full brightness (green on)
            self.blue.duty(0)    # Blue off
            await asyncio.sleep(interval)
            
            self.red.duty(0)     # Red off
            self.green.duty(0)   # Green off
            self.blue.duty(1023)  # Full brightness (blue on)
            await asyncio.sleep(interval)

    async def stop_blinking(self):
        """
        Stop the blinking process by setting all colors to off.
        """
        self.blinking = False
        self.red.duty(0)
        self.green.duty(0)
        self.blue.duty(0)
        print("Stopped blinking.")

    async def set_color(self, r=None, g=None, b=None):
        """
        Set the duty cycle for each LED.
        If a value is not provided, it will remain unchanged.
        :param r: Duty cycle for red (0-1023 or "on"/"off")
        :param g: Duty cycle for green (0-1023 or "on"/"off")
        :param b: Duty cycle for blue (0-1023 or "on"/"off")
        """
        if r is not None:
            if r == "on":
                self.red.duty(1023)
            elif r == "off":
                self.red.duty(0)
            else:
                self.red.duty(r)
        
        if g is not None:
            if g == "on":
                self.green.duty(1023)
            elif g == "off":
                self.green.duty(0)
            else:
                self.green.duty(g)
        
        if b is not None:
            if b == "on":
                self.blue.duty(1023)
            elif b == "off":
                self.blue.duty(0)
            else:
                self.blue.duty(b)

    async def color_cycle(self):
        """
        Cycle through red, green, and blue colors asynchronously.
        """
        print("Cycling through colors...")
        await self.set_color(r="on", g="off", b="off")  # Red on
        await asyncio.sleep(1)
        await self.set_color(r="off", g="on", b="off")  # Green on
        await asyncio.sleep(1)
        await self.set_color(r="off", g="off", b="on")  # Blue on
        await asyncio.sleep(1)

    async def rgb(self):
        """
        Cycle through red, green, and blue colors for the LED instance.
        """
        await self.set_color(1023, 0, 0)  # Red
        await asyncio.sleep(1)
        await self.set_color(0, 1023, 0)  # Green
        await asyncio.sleep(1)
        await self.set_color(0, 0, 1023)  # Blue
        await asyncio.sleep(1)

    async def random_color(self):
        """
        Set the LED to a random color within specified ranges.
        """
        r, g, b = random.randint(800, 1023), random.randint(0, 1), random.randint(0, 1)
        await self.set_color(r, g, b)
        await asyncio.sleep(1)

    async def rgb_cycle(self, led_pins):
        """
        Cycle through red, green, and blue for multiple LEDs asynchronously.
        :param led_pins: Dictionary of LED pin configurations.
        """
        for led_name, pins in led_pins.items():
            led = RGBController(pins["r"].pin, pins["g"].pin, pins["b"].pin)
            await led.color_cycle()

# Create two instances of the RGB LEDs
rgb1 = RGBController(7, 5, 6)
rgb2 = RGBController(11, 10, 9)

# Example usage
# asyncio.run(rgb1.color_cycle())  # Cycle through colors for rgb1
# asyncio.run(rgb2.blink(0.5))     # Blink colors for rgb2 with an interval of 0.5 seconds
# asyncio.run(rgb1.stop_blinking())  # Stop blinking for rgb1
# asyncio.run(rgb2.random_color())  # Set rgb2 to a random color
# asyncio.run(rgb1.rgb())           # Cycle through red, green, and blue for rgb1
