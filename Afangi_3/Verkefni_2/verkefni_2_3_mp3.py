from machine import Pin
import asyncio
from lib.dfplayer import DFPlayer

# DFPlayer Controller Class
class DFPlayerController:
    def __init__(self, uart_num, tx_pin, rx_pin):
        self.dfplayer = DFPlayer(uart_num)
        self.dfplayer.init(tx=tx_pin, rx=rx_pin)
    
    # Play track once
    async def play_audio(self, folder, file, volume=15):
        await self.dfplayer.wait_available()  # Ensure DFPlayer is ready
        await self.dfplayer.volume(volume)    # Set volume level
        await self.dfplayer.play(folder, file)  # Play specified file
    
    # Play repeatedly
    async def play_audio_repeat(self, folder, file, volume=15):
        await self.dfplayer.wait_available()  # Ensure DFPlayer is ready
        await self.dfplayer.volume(volume)    # Set volume level
        await self.dfplayer.mode(DFPlayer.MODE_REPEAT_FILE)
        await self.dfplayer.play(folder, file)  # Play specified file
            
            
    # Á eftir að bæta hérna við í klasann að hlátur tengist tíma
    # en skráin fyrir hláturinn a að vera i möppu 02 og heitir 002.mp3

# RGB LED Controller Class
class RGBController:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red = Pin(red_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        self.blue = Pin(blue_pin, Pin.OUT)

    async def blink(self, interval=0.5):
        while True:
            self.red.on()
            self.green.off()
            self.blue.off()
            await asyncio.sleep(interval)
            
            self.red.off()
            self.green.on()
            self.blue.off()
            await asyncio.sleep(interval)
            
            self.red.off()
            self.green.off()
            self.blue.on()
            await asyncio.sleep(interval)

# Main function to play music and blink lights
async def main_1():
    # Create Instance of the player
    player = DFPlayerController(uart_num=2, tx_pin=17, rx_pin=16)
    
    # Create instances of each rgb light
    rgb1 = RGBController(6, 5, 7)
    rgb2 = RGBController(9, 10, 11)

    # Run play_audio and blink concurrently
    await asyncio.gather(
        player.play_audio(1, 1),  # Plays file 1 in folder 1
        rgb1.blink(),             # Blinks the first set of RGB LEDs
        rgb2.blink()              # Blinks the second set of RGB LEDs
    )
# Main function to play music and blink lights
async def main_2():
    # Create Instance of the player
    player = DFPlayerController(uart_num=2, tx_pin=17, rx_pin=16)
    player2 = DFPlayerController(uart_num=2, tx_pin=17, rx_pin=16)
    
    # Create instances of each rgb light
    rgb1 = RGBController(6, 5, 7)
    rgb2 = RGBController(9, 10, 11)

    # Run play_audio and blink concurrently
    await asyncio.gather(
        player.play_audio_repeat(1, 1),  # Plays file 1 in folder 1
        player2.play_audio_repeat(2, 2),  # Plays file 1 in folder 1
        rgb1.blink(),             # Blinks the first set of RGB LEDs
        rgb2.blink()              # Blinks the second set of RGB LEDs
    )

# Run the main function
while True:
    asyncio.run(main_2())
