###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################


from machine import Pin, PWM
import time 

from car_components_files.motor_class import Motor
from car_components_files.addons import UltrasonicSensor, MPU6050
from car_components_files.settings_functions import log_message

        
###########################################################
 ##### ----- ----- Car Class And Methods ----- ----- #####
###########################################################
        
class Car:
    def __init__(self, motor_a, motor_b, stby_pin, ultrasonic_sensor):  # , mpu
                                                                    
        # Initialize motor objects with specific pins and PWM frequencies
        self.motor_a = motor_a
        self.motor_b = motor_b
        
        # Initialize Standby Pin
        self.stby = stby_pin
        
        # Initialize The UltraSonic Sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        
#         self.mpu = mpu
        
        self.show_car_status()
        
        # Extra properties        
        self.turn_speed_left_a = 0
        self.turn_speed_left_b = 475
        
        self.turn_speed_right_a = 520
        self.turn_speed_right_b = 0

        self.turn_duration_90 = 0.7
        self.turn_duration_180 = (2 * self.turn_duration_90) - 0.1
        self.turn_duration_270 = 3 * self.turn_duration_90
        self.turn_duration_360 = 4 * self.turn_duration_90
        
        
        
        
          ############################################
          ##### ----- Drive & Stop Methods ----- #####
          ############################################
    def drive_straight_with_correction(self, direction, gyro_bias=0, speed=None):
        correction_factor = 10  # Adjust based on your testing
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        log_message(f"Driving {direction}. Base Speed: A={self.motor_a.get_current_speed()}, B={self.motor_b.get_current_speed()}")

        initial_yaw = self.mpu.update_yaw() - gyro_bias  # Adjust initial yaw by gyro bias
        while True:
            current_yaw = self.mpu.update_yaw() - gyro_bias  # Adjust every reading by gyro bias
            yaw_error = current_yaw - initial_yaw  # Calculate yaw error

            if abs(yaw_error) > 0:  # If there's a noticeable yaw error
                if yaw_error < 0:
                    # Car is veering left, increase speed of left motor to correct
                    adjusted_speed_a = self.motor_a.get_current_speed() + abs(yaw_error) * correction_factor
                    adjusted_speed_b = self.motor_b.get_current_speed() - abs(yaw_error) * correction_factor
                    log_message(f"Correcting from left. Speed: A={adjusted_speed_a}, B={adjusted_speed_b}")
                else:
                    # Car is veering right, increase speed of right motor to correct
                    adjusted_speed_a = self.motor_a.get_current_speed() - abs(yaw_error) * correction_factor
                    adjusted_speed_b = self.motor_b.get_current_speed() + abs(yaw_error) * correction_factor
                    log_message(f"Correcting from right. Speed: A={adjusted_speed_a}, B={adjusted_speed_b}")
                
                self.motor_a.set_speed(adjusted_speed_a)
                self.motor_b.set_speed(adjusted_speed_b)

            time.sleep(0.1)  # Short delay for continuous monitoring


    # This way, the car drives and has a obstacle detection to true or false
    def drive_car(self, direction, duration=None, speed=None, obstacle_detection=False):
        # Record the start time
        start_time = time.time()  

        # Start Driving
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        log_message(f"Started driving in direction: {direction} and with speed: Motor A: {self.motor_a.get_current_speed()} Motor B: {self.motor_b.get_current_speed()}")
        
        # If obstacle_detection is True and no duration
        if obstacle_detection and not duration:
            # Proceed in chosen direction

            while True:
                distance = self.ultrasonic_sensor.measure_distance()
                log_message(f"\nMeasured Distance: {distance}")
                if distance < 50:
                    # Stop and back up slightly
                    self.stop_car()
                    time.sleep(2)  # Wait for 1 second to simulate backing up
                    
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
                        # If no clear path or both < 50cm, turn 90° more to the right, to face the back direction
                        log_message(f"Both ways less then 50cm")
                        self.turn_90('left')
                    # Wait 2 seconds before resuming driving or turning again
                    time.sleep(2)
                    
                    # After handling obstacle, resume driving
                    self.motor_a.drive(direction, speed)
                    self.motor_b.drive(direction, speed)
                
                time.sleep(0.2)
                
        elif duration:
            time.sleep(duration)
            self.stop_car()
            
        else:
            log_message(f"You need to specify either obstacle detection as True and no duration or specify duration")


    def stop_car(self):
        self.motor_a.stop()
        self.motor_b.stop()
        log_message(f"\nstop_car method called")

          
          
            #######################################
            ##### ----- Turning Methods ----- #####
            #######################################
    
    def turn(self, left_or_right):
        # Turn right with motor A 
        if left_or_right == 'right':
            self.motor_a.drive('forward', self.turn_speed_right_a)
            self.motor_b.stop()
        # Turn left with Motor B
        else:
            self.motor_b.drive('forward', self.turn_speed_left_b)
            self.motor_a.stop()
            
        log_message(f"\nTurning {left_or_right}.")
        
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
        log_message(f"\nCompleted 90° turn to the {left_or_right}.")
        
    # For 180° turns
    def turn_180(self, left_or_right):
        self.turn(left_or_right)
        time.sleep(self.turn_duration_180)
        self.stop_car()
        log_message(f"\nCompleted 180° turn to the {left_or_right}.")
    
    # For 360° circle turning
    def turn_360(self, left_or_right):
        self.turn(left_or_right)
        time.sleep(self.turn_duration_360)
        self.stop_car()
        log_message(f"\nCompleted 360° turn to the {left_or_right}.")
        
    # Print out the cars status
    def show_car_status(self):
        log_message("\nCar Status:")
        log_message(f"\nMotor A Status: \nForward={self.motor_a.forward.value()}, \nBackwards={self.motor_a.backwards.value()}, \nSpeed={self.motor_a.speed_pwm.duty()}, \nDefault speed={self.motor_a.default_speed}")
        log_message(f"\n\nMotor B Status: \nForward={self.motor_b.forward.value()}, \nBackwards={self.motor_b.backwards.value()}, \nSpeed={self.motor_b.speed_pwm.duty()}, \nDefault speed={self.motor_b.default_speed}")
    
#         # Adding MPU6050 status
#         accel_x, accel_y, accel_z = self.mpu.get_accel_data()
#         gyro_x, gyro_y, gyro_z = self.mpu.get_gyro_data()
#         log_message(f"\nMPU6050 Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
#         log_message(f"MPU6050 Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")
        
#         
#         
#     def drive_straight_with_target_speed(self, direction):
#     target_speed = 650  # Aim for a speed between 600 and 700
#     speed_correction_factor = 0.5  # Tune this based on testing
#     yaw_correction_factor = 10  # Adjust based on your testing
#     
#     # Initial drive command with default speeds
#     self.motor_a.drive(direction, 625)  # Starting speed
#     self.motor_b.drive(direction, 600)  # Starting speed
# 
#     initial_yaw = self.mpu.update_yaw()  # Get initial yaw to maintain
#     
#     while True:
#         current_yaw = self.mpu.update_yaw()
#         yaw_error = current_yaw - initial_yaw  # Calculate yaw error
# 
#         # Calculate speed adjustments based on yaw to correct direction
#         if yaw_error < 0:
#             # Adjusting speeds to correct from veering left
#             speed_adjustment_a = yaw_error * yaw_correction_factor
#             speed_adjustment_b = -yaw_error * yaw_correction_factor
#         else:
#             # Adjusting speeds to correct from veering right
#             speed_adjustment_a = -yaw_error * yaw_correction_factor
#             speed_adjustment_b = yaw_error * yaw_correction_factor
#         
#         # Get current speeds
#         current_speed_a = self.motor_a.get_current_speed()
#         current_speed_b = self.motor_b.get_current_speed()
# 
#         # Calculate speed error for each motor
#         speed_error_a = (target_speed - current_speed_a) * speed_correction_factor
#         speed_error_b = (target_speed - current_speed_b) * speed_correction_factor
# 
#         # Apply both yaw correction and target speed adjustment
#         adjusted_speed_a = max(0, min(1000, current_speed_a + speed_adjustment_a + speed_error_a))
#         adjusted_speed_b = max(0, min(1000, current_speed_b + speed_adjustment_b + speed_error_b))
# 
#         # Set the adjusted speeds
#         self.motor_a.set_speed(adjusted_speed_a)
#         self.motor_b.set_speed(adjusted_speed_b)
# 
#         log_message(f"Adjusted Speeds - A: {adjusted_speed_a}, B: {adjusted_speed_b}")
# 
#         time.sleep(0.1)  # Short delay for continuous monitoring
# 
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
        




#             while True:
#                 current_time = time.time()
#                 if (current_time - start_time) >= duration:
#                     self.stop_car()
#                     break  # Exit the loop after the duration has passed
   
   
#    
#     # This method adjusts speed based on the MPU6050 gyroscope Z value
#     def drive_straight_with_correction(self, direction, speed=None):
#         
#         target_z = -1.7  # Baseline Z-value for straight movement
#         threshold = 0.4  # Threshold for when to adjust motor speed
#         correction_factor = 10  # Adjust based on your testing
# 
#         # Start driving
#         self.motor_a.drive(direction, speed)
#         self.motor_b.drive(direction, speed)
#         log_message(f"Driving {direction}. Base Speed: A={self.motor_a.get_current_speed()}, B={self.motor_b.get_current_speed()}")
# 
#         while True:
#             _, _, z = self.mpu.get_gyro_data()  # Assuming self.mpu is your MPU6050 instance
#             error = z - target_z
# 
#             if abs(error) > threshold:
#                 if error < 0:
#                     # Decrease speed of motor A
#                     adjusted_speed = max(0, self.motor_a.get_current_speed() - abs(error) * correction_factor)
#                     log_message(f"Adjusting speed: Decreased Motor A to {adjusted_speed}")
#                 else:
#                     # Increase speed of motor A
#                     adjusted_speed = self.motor_a.get_current_speed() + abs(error) * correction_factor
#                     log_message(f"Adjusting speed: Increased Motor A to {adjusted_speed}")
#                 
#                 self.motor_a.set_speed(adjusted_speed)
#             
#             time.sleep(0.1)  # Short delay for continuous monitoring
# 
# 
