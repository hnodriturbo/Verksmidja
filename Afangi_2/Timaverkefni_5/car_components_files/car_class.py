###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################


from machine import Pin, PWM
import time 
import _thread
from car_components_files.motor_class import Motor
from car_components_files.addons import UltrasonicSensor, NeoPixelRing
from car_components_files.settings_functions import log_message

# MPU6050
from car_components_files.mpu6050_files.mpu6050_vector3d.imu import MPU6050, 
from car_components_files.mpu6050_files.mpu6050_vector3d.vector3d import Vector3d
        
        
        
                       ############
                      ##############
                     ################
                    ##################
        ##################      ##################
    ##################      ##       ##################
###########################################################

###########################################################
 ##### ----- ---- Car Class Initialization --- ----- #####
###########################################################
        
class Car:
    def __init__(self, motor_a, motor_b, stby_pin, ultrasonic_sensor, neopixel, mpu, buzzer, use_cop_lights=False):
        
        # Initialize motor objects with specific pins and PWM frequencies
        self.motor_a = motor_a
        self.motor_b = motor_b
        
        # Initialize Standby Pin
        self.stby = stby_pin
        
        # Initialize The UltraSonic Sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        
        # Initialize the NeoPixelRing
        self.neopixel = neopixel
        
        # Initialize the MPU6050
        self.mpu = mpu
        
        # Initialize the Buzzer
        self.buzzer = buzzer
        
        # Print out the cars main components status and details
        self.show_car_status()
        
        # Decide which lights to turn on based on the use_cop_lights flag
        if use_cop_lights:
            self.neopixel.start_cop_lights_thread()
            self.buzzer.start_cop_sounds()
        else:
            self.neopixel.car_on_lights()
            
        ### ----- Extra properties ----- ###
            
        # Flag to control the gyro-based speed adjustment thread
        self.adjust_speed_flag = False
        self.adjust_speed_thread = None    
        
        # Turn speed settings
        self.turn_speed_left_a = 300
        self.turn_speed_left_b = 300
        self.turn_speed_right_a = 300
        self.turn_speed_right_b = 300
        # Turn duration settings
        self.turn_duration_90 = 0.8
        self.turn_duration_180 = 1.5

        
                
    # Print out the status of operational items
    def show_car_status(self):
        log_message("\nCar Status:")
        log_message(f"\nMotor A Status: \nForward={self.motor_a.forward.value()}, \nBackwards={self.motor_a.backwards.value()}, \
                        \nSpeed={self.motor_a.speed_pwm.duty()}, \nDefault speed={self.motor_a.default_speed}")
        log_message(f"\n\nMotor B Status: \nForward={self.motor_b.forward.value()}, \nBackwards={self.motor_b.backwards.value()}, \
                        \nSpeed={self.motor_b.speed_pwm.duty()}, \nDefault speed={self.motor_b.default_speed}")
        
        
    # Method to stop both motors
    def stop_car(self):
        self.motor_a.stop()
        self.motor_b.stop()
        log_message(f"\nstop_car method called")
    
    
        
###########################################################      
    ##################      ##       ##################    
        ##################      ##################     
    ##################      ##       ##################
###########################################################       
        
###########################################################
  ########### Drive Car & Obstacle  Detection ###########
###########################################################

    # This way, the car drives and has a obstacle detection to true or false
    
    def drive_car(self, direction, duration=None, speed=None, obstacle_detection=False, cop_lights_and_sounds=False):
        
        # Start speed adjustment
        self.start_adjust_speed_thread()
        
        # Start Driving
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        log_message(f"Started driving in direction: {direction} and with speed: Motor A: {self.motor_a.get_current_speed()} Motor B: {self.motor_b.get_current_speed()}")
        
        
        # If obstacle_detection is True and is to be driving with obstacle detection
        if obstacle_detection:
            self.obstacle_detection(direction, speed)
        
        # Or if a duration is specified, then drive for that long
        elif duration:
            time.sleep(duration)
            self.stop_car()
        
        # Else, log error message
        else:
            log_message(f"You need to specify either obstacle detection as True and no duration or specify duration")



    # Method for driving with obstacle detection and gyro adjustments of speed
    def obstacle_detection(self, direction, speed=None):
        while True:
            # Check distance and go into choose_right_path if measured distance is below 50cm
            distance = self.ultrasonic_sensor.measure_distance()
            log_message(f"Measured distance: {distance}")
            if distance < 50:
                self.choose_right_path(direction, speed)
            time.sleep(0.5)
            
#             # Adjust speed of motor a based on gyro measurements
#             self.adjust_motor_speed_based_on_gyro()
    
    # Method for choosing the right path
    def choose_right_path(self, direction, speed=None):
        
        # Stop the adjustmenting of speed
        self.stop_adjust_speed_thread()
        
        # First stop the car and wait 2 seconds
        self.stop_car()
        time.sleep(2)
        
        # Turn left 90 degrees and measure distance
        self.turn_90('right')
        distance_right = self.ultrasonic_sensor.measure_distance()
        log_message(f"Measured distance to the right: {distance_right}")
        time.sleep(2)
        
        # Turn 180 degrees to the right (totaling 270 from original direction) and measure distance
        self.turn_180('right')
        distance_left = self.ultrasonic_sensor.measure_distance()
        log_message(f"Measured distance to the left: {distance_left}")
        time.sleep(2)
        
        # Compare distances and choose direction with more clearance
        log_message(f"Comparing distances and choosing direction")
        if distance_left >= distance_right and distance_left > 50:
            # No need to turn as car is already facing the direction with more clearance
            log_message(f"Distance left is more then distance right and more then 50cm. Continue to the left direction")
            pass
        
        elif distance_right >= distance_left and distance_right > 50:
            log_message(f"Distance right is more then distance left and more then 50cm. Turning back to left direction")
            self.turn_180('right')  # Turn back to the left direction
            
        else:
            # If no clear path or both < 50cm, turn 90° more to the left, to face the back direction
            log_message(f"Both ways less then 50cm")
            self.turn_90('left')
            
        # Wait 2 seconds before resuming driving or turning again
        time.sleep(2)
        
        # After handling obstacle, resume driving
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        
        # Start adjusting speed again to maintain direction
        self.start_adjust_speed_thread()
              
    
    
    
###########################################################      
    ##################      ##       ##################    
        ##################      ##################     
    ##################      ##       ##################
###########################################################       
        
###########################################################
  ############# ----- Turning Methods ----- #############
###########################################################  
    
    ##### ----- Turning method ----- #####
        
    def turn(self, left_or_right):
        # Turn right 
        if left_or_right == 'right':
            # First log/print out that we are starting the turn
            log_message(f"Starting turn and turn signal blinking to the right")
            
            # Only use the turn signals if the cop lights are not on
            if not self.neopixel.cop_lights_flag:
                # Turn on the turning signal to the right
                self.neopixel.turn_signal_right()
            
            # Turn by driving the motors in opposite directions to turn on the spot
            self.motor_a.drive('forward', self.turn_speed_right_a)
            self.motor_b.drive('backwards', self.turn_speed_left_b)
            
        # Turn left
        elif left_or_right == 'left':
            log_message(f"Starting turn and turn signal blinking to the left")
            
            # Only use the turn signals if the cop lights are not on
            if not self.neopixel.cop_lights_flag:
                # Turn on the turning signal to the right
                self.neopixel.turn_signal_left()
            
            # Turn by driving the motors in opposite directions to turn on the spot
            self.motor_b.drive('forward', self.turn_speed_left_b)
            self.motor_a.drive('backwards', self.turn_speed_left_a)
        
        # log/print that we are now in the turning process
        log_message(f"\nTurning {left_or_right}.")

      
    ##### ----- Use turn method to execute turns ----- #####
    def turn_90(self, left_or_right):
        # Execute turn
        self.turn(left_or_right)
        # Turning
        time.sleep(self.turn_duration_90)
        # Stop car
        self.stop_car()
        
        # Only use the turn signals if the cop lights are not on
        if not self.neopixel.cop_lights_flag:
            # Stop the turn signal thread
            self.neopixel.stop_turn_signal_thread()
        
        
        # Print out completetion of turning
        log_message(f"\nCompleted 90° turn to the {left_or_right}. \nStopped the turn_signal_thread()")
        

    # For 180° turns
    def turn_180(self, left_or_right):
        # Execute turn
        self.turn(left_or_right)
        # Sleep for the turn duration
        time.sleep(self.turn_duration_180)
        # Stop car after turning
        self.stop_car()
        
        # Only use the turn signals if the cop lights are not on
        if not self.neopixel.cop_lights_flag:
            # Stop the turn signal thread
            self.neopixel.stop_turn_signal_thread()
        
        log_message(f"\nCompleted 180° turn to the {left_or_right}. \nStopped the turn_signal_thread()")
    
    
###########################################################      
    ##################      ##       ##################    
        ##################      ##################     
    ##################      ##       ##################
###########################################################       
        
###########################################################
  ########## ----- Gyro Speed Adjustment ----- ##########
###########################################################
        
    # Start the adjust speed thread
    def start_adjust_speed_thread(self):
        if not self.adjust_speed_thread:
            self.adjust_speed_flag = True
            self.adjust_speed_thread = _thread.start_new_thread(self.adjust_motor_speed_based_on_gyro, ())

    # Stop the adjust speed thread
    def stop_adjust_speed_thread(self):
        self.adjust_speed_flag = False
        self.adjust_speed_thread = None
        
    # User the calibrated gyro adjustments to zero the measurement (ish)   
    def adjust_motor_speed_based_on_gyro(self):
        while self.adjust_speed_flag:
            _, _, z = self.mpu.read_calibrated_gyro()  # Get Z-axis gyro measurement
            current_speed = self.motor_a.get_current_speed()
            
            if z > 0.3:  # Turning left
                new_speed = max(0, min(current_speed + 10, 1023))
            elif z < -0.3:  # Turning right
                new_speed = max(0, min(current_speed - 10, 1023))
            else:
                new_speed = current_speed
            
            if new_speed != current_speed:
                self.motor_a.set_speed(new_speed)
                log_message(f"Adjusting Motor A speed to {new_speed}.")
            time.sleep(0.1)


###########################################################
  ############ ----- This is in imu.py ----- ############
###########################################################

# Ég gerði þessi tvö method inn i imu.py - það var einfaldara að gera það þar
# Það sem þetta gerir er að taka 100 mælingar, plúsa þær allar saman og deila
# svo með fjölda mælinga til að fá meðaltal. Svo nota ég annað fall til að lesa
# gyro z value sem er hægri og vinstri og þegar ég er með núllið þá get eg breytt
# hraða bílsins ef gildið fer yfir ákveðið mikið í gyroscope-inum. Ef gildið
# fer akveðið yfir valin mörk, þá breytir hann hraðanum a einu hjóli bílsins til
# að leiðrétta braut bílsins og halda honum á beinni braut.

# Þetta var skemmtilegt og erfitt að gera, en tókst fyrir rest.

# 
#     def calibrate_gyro(self, samples=100):
#         print("Calibrating gyroscope... Stay still...")
#         offset_x, offset_y, offset_z = 0, 0, 0
#         for _ in range(samples):
#             self.update()  # Updates the sensor readings
#             gx, gy, gz = self.gyro.xyz  # Get current Gyroscope values
#             offset_x += gx
#             offset_y += gy
#             offset_z += gz
#             sleep_ms(10)  # Short delay between readings
# 
#         self.gyro_offset_x = offset_x / samples
#         self.gyro_offset_y = offset_y / samples
#         self.gyro_offset_z = offset_z / samples
#         print("Gyroscope calibrated.")
# 
#     def read_calibrated_gyro(self):
#         """
#         Returns the calibrated gyroscope values by subtracting the offsets calculated during calibration.
#         """
#         self.update()  # Update sensor readings
#         gx, gy, gz = self.gyro.xyz  # Get current gyro values
#         return gx - self.gyro_offset_x, gy - self.gyro_offset_y, gz - self.gyro_offset_z
# 



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
                
