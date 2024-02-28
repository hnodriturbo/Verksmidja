        #########################################
        ##### ----- Hreiðar Pétursson ----- #####
        ### -- Búið til 10-14 febrúar 2024 -- ###
        #########################################

from machine import Pin, PWM
import time 

# I decided to utilize and organize my code to make this a good and
# as much readable, reusable and understandable coding. Also for practise.


# Here i decided to use my coding skills for utilization and organize this into a dictionary
def initialize_pins():
    pins = {
        # Motor A
        'forward_pin_A': Pin(11, Pin.OUT),
        'backwards_pin_A': Pin(10, Pin.OUT),
        'speed_pwm_A': PWM(Pin(17, Pin.OUT), freq=10000),
        # Motor B
        'forward_pin_B': Pin(13, Pin.OUT),
        'backwards_pin_B': Pin(12, Pin.OUT),
        'speed_pwm_B': PWM(Pin(16, Pin.OUT), freq=10000),
        # Standby Pin
        'stby': Pin(8, Pin.OUT),
        # Ultrasonic Sensor
        'echo': Pin(39, Pin.IN),
        'trig': Pin(38, Pin.OUT),
    }
    return pins


###########################################################
 #### ----- ----- Motor Class And Methods ----- ----- ####
###########################################################

class Motor:
    def __init__(self, forward, backwards, speed_pwm, default_speed) -> None:
        self.forward = forward
        self.backwards = backwards
        self.speed_pwm = speed_pwm
        self.default_speed = default_speed
        self.current_speed = default_speed
        
    
    def set_speed(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.speed_pwm.duty(int(speed))
        self.current_speed = speed
        
    def get_current_speed(self):
        return self.current_speed
    
    # Method for driving both forward and backwards
    def drive(self, direction, speed=None):
        # Drive motor forward
        if direction == 'forward':
            self.forward.value(1)
            self.backwards.value(0)
        # Drive Motor Backwards
        elif direction == 'backwards':
            self.forward.value(0)
            self.backwards.value(1)
        elif direction == 'stop':
            self.stop()
        # In case of some errors
        else:
            print("Invalid Direction")
            return
        # Set the speed to the selected speed 
        # (if there is none speed value, then it reverts to the default speed)
        self.set_speed(speed)
    
    def stop(self):
        self.set_speed(0)

###########################################################
###########################################################





###########################################################
 ##### ----- ----- Car Class And Methods ----- ----- #####
###########################################################
        
class Car:
    def __init__(self, motor_a, motor_b, stby_pin, ultrasonic_sensor):
        
        # Initialize motor objects with specific pins and PWM frequencies
        self.motor_a = motor_a
        self.motor_b = motor_b
        
        # Initialize Standby Pin
        self.stby = stby_pin
        
        # Initialize The UltraSonic Sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        
        
        
        # Extra properties        
        self.turn_speed_left_a = 230
        self.turn_speed_left_b = 300
        
        self.turn_speed_right_a = 300 
        self.turn_speed_right_b = 230

        self.turn_duration_90 = 0.8
        #self.turn_duration_90 = 0.6455
        self.turn_duration_180 = 2 * self.turn_duration_90
        self.turn_duration_270 = 3 * self.turn_duration_90
        self.turn_duration_360 = (4 * self.turn_duration_90) - 0.135
        
        
        
        
          ############################################
          ##### ----- Drive & Stop Methods ----- #####
          ############################################

    # This way, the car drives and prints measurements every 1 second
    # If measured distance is below 50cm, this stops the car and exits
    # the method, otherwise it continues until duration is reached.
    
    def drive_car(self, direction, duration=None, speed=None):
        
        # Set the start time
        start_time = time.time()
        
        # reasons_for_stopping = ["Time ran out.", "Obstacle detected within 50cm] # This is only if it has a duration"]
        
        # Start Driving
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        

        
        while True:
            # Set the current time
            current_time = time.time()
            
            # Measure distance
            distance = self.ultrasonic_sensor.measure_distance()
            print(f"\nMeasured Distance: {distance}")
            
            # Check for stopping condition based on distance
            if distance < 50:
                self.stop_car()
                print(f"\nExiting the drive method: Obstacle detected within 50cm")
                return True
            
            # If duration is put in as an argument, then this doesn't run (car drives until < 50cm)
            if duration is not None and (current_time - start_time) >= duration:
                self.stop_car()
                print(f"\nExiting the drive method: Time ran out")
                return False # Timed out
            
            # This is the measure printing delays
            time.sleep(0.2)
        
        print("\nExiting the drive method and the car should be stopped right now.")

              
    def stop_car(self):
        self.motor_a.stop()
        self.motor_b.stop()
        print(f"\nstop_car method called")

          
          
            #######################################
            ##### ----- Turning Methods ----- #####
            #######################################
    
    def turn(self, left_or_right):
        # Turn right with motor A 
        if left_or_right == 'right':
            self.motor_a.drive('forward', self.turn_speed_right_a)
            self.motor_b.drive('backwards', self.turn_speed_right_b)
        # Turn left with Motor B
        else:
            self.motor_b.drive('forward', self.turn_speed_left_b)
            self.motor_a.drive('backwards', self.turn_speed_left_a)
            
        print(f"\nTurning {left_or_right}.")
        
        # Stop the other motor
        #(self.motor_b if left_or_right == 'right' else self.motor_a).stop()
      
    # Method for turning 90°
    def turn_90(self, left_or_right):
        # Execute turn
        self.turn(left_or_right)
        # Turning
        time.sleep(self.turn_duration_90)
        # Stop car
        self.stop_car()
        # Print out completetion of turning
        print(f"\nCompleted 90° turn to the {left_or_right}.")
        
#     # For 180° turns, use the 90° twice
#     def turn_180(self, left_or_right, speed=None):
#         self.turn(left_or_right, speed)
#         time.sleep(self.turn_duration_180)
#         self.stop_car()
#         print(f"\nMade 180° turn")
        
    def turn_360(self, left_or_right):
        self.turn(left_or_right)
        time.sleep(self.turn_duration_360)
        self.stop_car()
        print(f"\nCompleted 360° turn to the {left_or_right}.")
        
    # Example method in Car class to demonstrate functionality
    def show_car_status(self):
        print("\nCar Status:\n")
        print(f"\nMotor A Status: \nForward={self.motor_a.forward.value()}, \nBackwards={self.motor_a.backwards.value()}, \nSpeed={self.motor_a.speed_pwm.duty()}, \nDefault speed={self.motor_a.default_speed}")
        print(f"\n\nMotor B Status: \nForward={self.motor_b.forward.value()}, \nBackwards={self.motor_b.backwards.value()}, \nSpeed={self.motor_b.speed_pwm.duty()}, \nDefault speed={self.motor_b.default_speed}")
        
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




#     def turn(self, left_or_right, speed=None):
#         
#         # First check if parameter left or right is correct
#         if left_or_right not in ['left', 'right']:
#             print("\nInvalid direction for turn_90 method (valid is: right or left).")
#             return
#     
#         speed_a = (self.turn_speed_right_a if speed is None else speed) if left_or_right == 'right' else 0 
#         speed_b = (self.turn_speed_left_b if speed is None else speed) if left_or_right == 'left' else 0
#         
#         
#         self.motor_a.drive('forward' speed_a) if left_or_right == 'right' else self.motor_a.stop()
#         self.motor_b.drive('forward' speed_b) if left_or_right == 'left' else self.motor_b.stop()
#         
#         
#         # Print directions of motors for debugging and information purpose
#         print(f"\nMotor A direction = {direction_a} \nMotor A Current Speed = {self.motor_a.get_current_speed()} \nMotor B direction = {direction_b}\nMotor B Current Speed = {self.motor_b.get_current_speed()}")
#     
#   


a