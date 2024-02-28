###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
########################################################### 
 
from machine import Pin, PWM, SoftI2C
import struct
import time
import neopixel
import _thread
from car_components_files.settings_functions import initialize_pins, log_message


                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################

###########################################################
 ### ---- --- My NeoPixelRing Class & Methods --- ---- ###
###########################################################

class NeoPixelRing:
    def __init__(self, neopixel_s, neopixel_num_leds) -> None:
        # Initialize the instance
        self.neopixel = neopixel.NeoPixel(neopixel_s, neopixel_num_leds)
        self.neopixel_num_leds = neopixel_num_leds
        log_message("Initialized with num LEDs:", neopixel_num_leds)
        
        
        # Set the brightness to half
        self.brightness = 0.2
        log_message(f"Brightness set to: {self.brightness}")
        
        
        # Additional settings and flags for the turning signals
        self.blink_duration = 0.25  # Set default blink duration
        self.turn_signal_direction = None
        self.turn_signal_flag = False
        self.turn_signal_thread = None
    
    
        # Additional settings and flags for the car turned on leds
        self.cycle_animation_car_on_flag = False
        self.cycle_animation_car_on_thread = None
        
        # Additional settings and flags for the cop lights
        self.cop_lights_flag = False
        self.cop_lights_thread = None
        
        
        # Dictionary of colors
        self.light_colors = {
            'Red': (255, 0, 0),
            'Green': (0, 255, 0),
            'Blue': (0, 0, 255),
            'Yellow': (255, 255, 0),
            'Orange': (255, 165, 0),
            'Magenta': (255, 0, 255),
            'Cyan': (0, 255, 255),
            'Purple': (160, 32, 240),
            'Pink': (255, 192, 203),
            'Maroon': (128, 0, 0),
            'Olive': (128, 128, 0),
            'Dark Green': (0, 128, 0),
            'Dark Purple': (128, 0, 128),
            'Teal': (0, 128, 128),
            'Navy': (0, 0, 128),
            'Steel Blue': (70, 130, 180),
            'Tan': (210, 180, 140),
            'Dark Olive': (0, 100, 0),
            'Dark Goldenrod': (184, 134, 11),
            'Dark Gray': (169, 169, 169),
        }
        log_message(f"Created the colors dictionary")
    
    
    # Clear the lights
    def clear(self):
        for i in range(self.neopixel_num_leds):
            self.neopixel[i] = (0, 0, 0)
        self.neopixel.write()
    
    def clear_pixel(self, led_index):
        self.neopixel[led_index] = (0, 0, 0)
        self.neopixel.write()

    # Vill skrifa hérna á islensku. Ég gerði mikið af útgáfum af þessu falli eða method/function
    # Ég endaði á að fara í gömul æfingaverkefni þar sem við unnum með tuple, map og lambda því
    # ég fann út að það væri lang hentugasta leiðin til að margfalda tvisvar sinnum valið "brightness"
    # í þessu litar tuple því án þess að margfalda tvisvar verður þetta eins og maður sé að still i alvöru
    # brightness en maður er samt bara i rauninni að velja daufari en svipaðan/sama lit.
    def set_brightness(self, color, brightness):
        adjusted_brightness = brightness ** 2
        return tuple(map(lambda c: int(c * adjusted_brightness), color))

          

    # This method writes the color to the neopixel led after adjusting the brightness
    def set_pixel(self, led_index, color, brightness=None):
        
        # Adjust the color brightness if a specific brightness level is provided
        if brightness is not None:
            adjusted_color = self.set_brightness(color, brightness)
        
        # If no brightness was used as argument, then use the self.brightness value
        else:
            adjusted_color = self.set_brightness(color, self.brightness)
            
        # Write the color to the specific led index
        self.neopixel[led_index] = adjusted_color
        self.neopixel.write()
 
    
########################################################
        ###### Standby Car Lights Thread #####
########################################################
    
    # Start the car on cycle animation thread
    def start_cycle_animation_car_on_thread(self):
        self.cycle_animation_car_on_flag = True
        if not self.cycle_animation_car_on_thread:
            self.cycle_animation_car_on_thread = _thread.start_new_thread(self.cycle_animation_car_on, ())
            
    def stop_cycle_animation_car_on_thread(self):
        self.cycle_animation_car_on_flag = False
        time.sleep(0.5)
        self.cycle_animation_car_on_thread = None
    
    # Animation to light up leds in circle motion and iterate over each color
    def cycle_animation_car_on(self):
        # Start the while loop that continues constantly until stopped
        while self.cycle_animation_car_on_flag:
            # Iterate over the dictionary
            for color_name, color_value in self.light_colors.items():
                # Create the circling effect for the current color
                for led_index in range(self.neopixel_num_leds):
                    # Set the current led to the current color
                    self.set_pixel(led_index, color_value)
                    log_message(f"led with index {led_index} was set to color: {color_value}")
                    # How long the led is turned on:
                    time.sleep(0.1)

                    if led_index > 1:
                        self.clear_pixel(led_index - 2)
                    elif led_index == 1:
                        self.clear_pixel(self.neopixel_num_leds - 1)
                    elif led_index == 0:
                        self.clear_pixel(self.neopixel_num_leds - 2)
                    
# Most simple way to do this is like this but i wanted the coding to be more simpler logic
#                     led_to_turn_off = (led_index - 2) % self.neopixel_num_leds
#                     self.clear_pixel(led_to_turn_off)

 
                # Check if the flag is still true to continue or break the loop
                if not self.cycle_animation_car_on_flag:
                    break
                
                # Optional pause between colors if desired
                # time.sleep(1)
                
        # If while loop is broken, clear all leds
        self.clear()

    # Turn on the car lights
    def car_on_lights(self):
        if not self.cycle_animation_car_on_flag:
            self.start_cycle_animation_car_on_thread()
             
    
########################################################
        ###### Turning Signals and Threads #####
########################################################
    
    # Start turn signal thread
    def start_turn_signal_thread(self, direction):
        if not self.turn_signal_thread:
            self.stop_cycle_animation_car_on_thread()
            self.turn_signal_direction = direction
            self.turn_signal_thread = _thread.start_new_thread(self.turn_signal_blink, ())
         
    # Stop turn signal thread
    def stop_turn_signal_thread(self):
        self.turn_signal_flag = False
        self.turn_signal_thread = None
        # After stopping the turn signals start the cycle animation again
        self.car_on_lights()
        
    # Handle the turn signal blinking
    def turn_signal_blink(self):
        while self.turn_signal_flag:
            
            # Set the color and the brightness
            color = self.light_colors['Orange']
            
            # Use set_pixel to write the color to specific indexes of leds (passing brightness is optional now)
            if self.turn_signal_direction == 'right':
                for i in range(self.neopixel_num_leds - 1):
                    if i < 5:
                        self.set_pixel(i, color, 0.1)  # Passing brightness directly
            elif self.turn_signal_direction == 'left':
                for i in range(self.neopixel_num_leds):
                    if i > 3 or i == 0:
                        self.set_pixel(i, color, 0.1)  # Passing brightness directly
                        
            
            time.sleep(self.blink_duration)
            self.clear()
            time.sleep(self.blink_duration)
            
    def turn_signal_right(self):
        if not self.turn_signal_flag:
            self.turn_signal_flag = True
            self.start_turn_signal_thread('right')

    def turn_signal_left(self):
        if not self.turn_signal_flag:
            self.turn_signal_flag = True
            self.start_turn_signal_thread('left')

########################################################
          ###### Cop lights and Threads #####
########################################################

    def start_cop_lights_thread(self):
        # First stop the animation car on thread and turn signal thread
        if self.cycle_animation_car_on_flag:
            self.stop_cycle_animation_car_on_thread()
        if self.turn_signal_flag:
            self.stop_turn_signal_thread()
        
        # Start cop lights thread if not already running
        if not self.cop_lights_thread:
            self.cop_lights_flag = True
            self.cop_lights_thread = _thread.start_new_thread(self.cop_lights_animation, ())
            
         
    def stop_cop_lights_thread(self):
        # Stop cop lights animation
        self.cop_lights_flag = False
        time.sleep(0.5)  # Ensure the animation loop can exit
        self.cop_lights_thread = None
        # Clear LEDs as a cleanup step
        self.clear()

    def cop_lights_animation(self):
        while self.cop_lights_flag:
            for i in range(self.neopixel_num_leds):
                self.set_pixel(i, self.light_colors['Red'])
            time.sleep(0.3)  # Control speed of flashing
            self.clear()  # Clear lights between flashes
            for i in range(self.neopixel_num_leds):
                self.set_pixel(i, self.light_colors['Blue'])
            time.sleep(0.3)
            self.clear()

            if not self.cop_lights_flag:
                break
        # Clear lights when animation stops
        self.clear()

    # Turn on the car cop lights
    def turn_on_cop_lights(self):
        if not self.cop_lights_flag:
            self.start_cop_lights_thread()
 
 
###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################
    
###########################################################
 #### ----- Ultrasonic Sensor Class And Methods ----- ####
###########################################################
        
class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin


    def measure_distance(self):
        # Trigger the measurement
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        
        # Wait for the echo to start
        while not self.echo.value():
            pass
        start = time.ticks_us()
        
        # Wait for the echo to end
        while self.echo.value():
            pass
        end = time.ticks_us()
        
        # Calculate the duration and distance
        duration = time.ticks_diff(end, start)
        distance = (duration * 0.0343) / 2  # Convert time to distance
        
        return distance


###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################
        
###########################################################
 ### ---- -----  My Buzzer Class & Methods  ----- ---- ###
###########################################################

## LATEST ##
class Buzzer:
    
    def __init__(self, buzzer_pin):
        self.buzzer = PWM(Pin(buzzer_pin))
        self.buzzer.freq(440)  # A4 as a default, reasonable starting point
        self.buzzer.duty(0)  # Duty cycle to 0 to effectively 'mute' it initially
        self.playing_sound = False
        
        # Initialize cop_sounds with notes renamed
        self.cop_sounds = {'G4': 392, 'C5': 523}
        
        # A dictionary of tones with note names and their frequencies
        self.tones = {
            'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
            'G4': 392.00, 'A4': 440.00, 'B4': 493.88,
            'C5': 523.25, 'D5': 587.33, 'E5': 659.25, 'F5': 698.46,
            'G5': 783.99, 'A5': 880.00, 'B5': 987.77,
            'C6': 1046.50, 'D6': 1174.66, 'E6': 1318.51, 'F6': 1396.91,
            # Extending the dictionary to cover more notes if desired
            'G6': 1567.98, 'A6': 1760.00, 'B6': 1975.53,
            'C7': 2093.00, 'D7': 2349.32, 'E7': 2637.02, 'F7': 2793.83,
            'G7': 3135.96, 'A7': 3520.00, 'B7': 3951.07,
        }
        
    def start_cop_sounds(self):
        if not self.playing_sound:
            self.playing_sound = True
            _thread.start_new_thread(self.play_cop_sounds, ())

    def stop_cop_sounds(self):
        self.playing_sound = False
        self.buzzer.duty(0)  # Stop the sound


    def play_cop_sounds(self):
        while self.playing_sound:
            for tone_name, tone_freq in self.cop_sounds.items():
                if not self.playing_sound:
                    break
                self.buzzer.freq(tone_freq)  # Set the frequency to the current tone
                self.buzzer.duty(512)  # Set duty cycle to 50% for sound
                time.sleep(0.5)  # Duration of each tone
            self.buzzer.duty(0)  # Stop the sound between repeats
            time.sleep(0.1)  # Short pause between repeats of the tone sequence
            

###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################       
        
        
        
                # er ekki að nota þennan #
###########################################################
 ### ---- ----- My MPU6050  Class & Methods ----- ---- ###
###########################################################

class MPU6050:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.address = 0x68  # Device I2C address
        self._accel_reg = 0x3B
        self._gyro_reg = 0x43
        self._power_mgmt_1 = 0x6B
        # Corrected from self._power_fear to self._power_mgmt_1
        self.i2c.writeto_mem(self.address, self._power_mgmt_1, b'\x00')  # Wake up the MPU6050
        time.sleep_ms(100)  # Ensure MPU6050 is powered up before proceeding

    def _read_data(self, reg, bytes=6):
        """Reads bytes from the given register."""
        data = self.i2c.readfrom_mem(self.address, reg, bytes)
        return struct.unpack(">hhh", data)

    def get_accel_data(self):
        """Returns accelerometer data."""
        ax, ay, az = self._read_data(self._accel_reg)
        # Convert from raw data to 'g' values
        # Assuming the accelerometer is set to ±2g range
        # 16,384 LSB/g (least significant bit per g)
        ax, ay, az = [a / 16384.0 for a in [ax, ay, az]]
        return ax, ay, az

    def get_gyro_data(self):
        """Returns gyroscope data."""
        gx, gy, gz = self._read_data(self._gyro_reg)
        # Convert from raw data to degrees per second
        # Assuming the gyroscope is set to ±250 degrees/s range
        # 131 LSB/(degrees/s)
        gx, gy, gz = [g / 131.0 for g in [gx, gy, gz]]
        return gx, gy, gz

 
###########################################################
    ##################      ##       ##################
        ##################      ##################
                    ##################
                     ################
                      ##############
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################



