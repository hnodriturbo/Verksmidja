from machine import Pin
import asyncio
import time
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

    # Stop the audio from playing continuously
    async def stop_audio(self):
        await self.dfplayer.stop()  # Stop the current audio playback
        print("Audio playback stopped.")
        
# RGB LED Controller Class
class RGBController:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red = Pin(red_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        self.blue = Pin(blue_pin, Pin.OUT)
        self.blinking = True

    async def blink(self, interval=0.5):
        while self.blinking:
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

    async def stop_blinking(self):
        self.blinking = False
        self.red.off()
        self.green.off()
        self.blue.off()
        print("Stopped blinking.")

# Main function to play music and blink lights
async def main_1():
    # Create Instance of the player
    player = DFPlayerController(uart_num=2, tx_pin=17, rx_pin=16)
    
    # Create instances of each rgb light
    rgb1 = RGBController(6, 5, 7)
    rgb2 = RGBController(9, 10, 11)

    # Run play_audio_repeat and blink concurrently
    await asyncio.gather(
        player.play_audio_repeat(1, 1),  # Plays file 1 in folder 1
        rgb1.blink(),                    # Blinks the first set of RGB LEDs
        rgb2.blink(),                    # Blinks the second set of RGB LEDs
        stop_after_delay(player, rgb1, rgb2, 10)     # Stop playback and lights after 10 seconds
    )
# Main function to play music and blink lights
async def main_2():
    
        
    # Create Instance of the player
    player = DFPlayerController(uart_num=2, tx_pin=17, rx_pin=16)
    
    # Create instances of each rgb light
    rgb1 = RGBController(6, 5, 7)
    rgb2 = RGBController(9, 10, 11)
    
    try:
        # Run play_audio_repeat and blink concurrently
        await asyncio.gather(
            player.play_audio_repeat(2, 2),  # Plays file 2 in folder 2
            rgb1.blink(),                    # Blinks the first set of RGB LEDs
            rgb2.blink(),                    # Blinks the second set of RGB LEDs
            stop_after_delay(player, rgb1, rgb2, 10)     # Stop playback and lights after 10 seconds
        )
    finally:
        # Ensure that audio stops when the script is terminated
        print("\nStopping playback...")
        await player.stop_audio()


# Bjó til sérstakt async function til að stoppa spilunina því lagið spilar stanslaust
# meira segja þó maður ýtir a stopp takkann !!!

# Function to stop playback after a delay
async def stop_after_delay(player, rgb1, rgb2, delay):
    await asyncio.sleep(delay)
    await player.stop_audio()
    await rgb1.stop_blinking()
    await rgb2.stop_blinking()

# Run the main function
asyncio.run(main_1())
