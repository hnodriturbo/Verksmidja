###########################################################

#             while True:
#                 current_time = time.time()
#                 if (current_time - start_time) >= duration:
#                     self.stop_car()
#                     break  # Exit the loop after the duration has passed
# Set the start time
# start_time = time.time()

# reasons_for_stopping = ["Time ran out.", "Obstacle detected within 50cm] # This is only if it has a duration"]


#
#
#     def detect_obstacle_and_navigate(self):
#         while True:
#             distance = self.ultrasonic_sensor.measure_distance()
#             if distance < 50:
#                 # Stop and back up slightly
#                 self.stop_car()
#                 time.sleep(1)  # Wait for 1 second to simulate backing up
#
#                 # Turn left 90 degrees and measure distance
#                 self.turn_90('left')
#                 distance_left = self.ultrasonic_sensor.measure_distance()
#
#                 # Turn 180 degrees to the right (totaling 270 from original direction) and measure distance
#                 self.turn_180('right')
#                 distance_right = self.ultrasonic_sensor.measure_distance()
#
#                 # Compare distances and choose direction with more clearance
#                 if distance_left > 50 and distance_left >= distance_right:
#                     self.turn_180('left')  # Turn back to the left direction
#                 elif distance_right > 50:
#                     # No need to turn as car is already facing the direction with more clearance
#                     pass
#                 else:
#                     # If no clear path, turn 180 degrees to face original direction
#                     self.turn_180('right')
#
#                 # Proceed in chosen direction
#                 self.drive_car('forward', duration=None, speed=None)
#             else:
#                 self.drive_car('forward', duration=None, speed=None)
#
#         while True:
#             # Set the current time
#             current_time = time.time()

# Measure distance
#             distance = self.ultrasonic_sensor.measure_distance()
#             print(f"\nMeasured Distance: {distance}")
#
#             # Check for stopping condition based on distance
#             if distance < 50:
#                 self.stop_car()
#                 print(f"\nExiting the drive method: Obstacle detected within 50cm")
#                 return True
#
#             # If duration is put in as an argument, then this doesn't run (car drives until < 50cm)
#             if duration is not None and (current_time - start_time) >= duration:
#                 self.stop_car()
#                 print(f"\nExiting the drive method: Time ran out")
#                 return False # Timed out
#
#             # This is the measure printing delays
#             time.sleep(0.2)
#
#         print("\nExiting the drive method and the car should be stopped right now.")


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

# Set the start time
# start_time = time.time()

# reasons_for_stopping = ["Time ran out.", "Obstacle detected within 50cm] # This is only if it has a duration"]


#
#
#     def detect_obstacle_and_navigate(self):
#         while True:
#             distance = self.ultrasonic_sensor.measure_distance()
#             if distance < 50:
#                 # Stop and back up slightly
#                 self.stop_car()
#                 time.sleep(1)  # Wait for 1 second to simulate backing up
#
#                 # Turn left 90 degrees and measure distance
#                 self.turn_90('left')
#                 distance_left = self.ultrasonic_sensor.measure_distance()
#
#                 # Turn 180 degrees to the right (totaling 270 from original direction) and measure distance
#                 self.turn_180('right')
#                 distance_right = self.ultrasonic_sensor.measure_distance()
#
#                 # Compare distances and choose direction with more clearance
#                 if distance_left > 50 and distance_left >= distance_right:
#                     self.turn_180('left')  # Turn back to the left direction
#                 elif distance_right > 50:
#                     # No need to turn as car is already facing the direction with more clearance
#                     pass
#                 else:
#                     # If no clear path, turn 180 degrees to face original direction
#                     self.turn_180('right')
#
#                 # Proceed in chosen direction
#                 self.drive_car('forward', duration=None, speed=None)
#             else:
#                 self.drive_car('forward', duration=None, speed=None)
#
#         while True:
#             # Set the current time
#             current_time = time.time()

# Measure distance
#             distance = self.ultrasonic_sensor.measure_distance()
#             print(f"\nMeasured Distance: {distance}")
#
#             # Check for stopping condition based on distance
#             if distance < 50:
#                 self.stop_car()
#                 print(f"\nExiting the drive method: Obstacle detected within 50cm")
#                 return True
#
#             # If duration is put in as an argument, then this doesn't run (car drives until < 50cm)
#             if duration is not None and (current_time - start_time) >= duration:
#                 self.stop_car()
#                 print(f"\nExiting the drive method: Time ran out")
#                 return False # Timed out
#
#             # This is the measure printing delays
#             time.sleep(0.2)
#
#         print("\nExiting the drive method and the car should be stopped right now.")


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


##########################################################
#####  ##### ----- Storage Code Below ----- #####  #####
##########################################################

# When I was finding out the right and same speed for both motors I
# found out that 430 for motor A was the same speed as 512 for motor B
# a_speed = 430 # These two make up about the same speed
# b_speed = 512 #             - || -

# Set the turn time (using speeds 430 and 512 makes this almost a 90° turn)
# turn_duration = 0.4


# Fallið sem mælir vegalengd i sentimetrum
# def measure_distance(trig, echo):
#     trig.value(1)
#     time.sleep_us(10)
#     trig.value(0)
#
#     while not echo.value():
#         pass
#     start = time.ticks_us()
#
#     while echo.value():
#         pass
#     end = time.ticks_us()
#
#     duration = time.ticks_diff(end, start)
#
#     distance = (duration * 0.0343) / 2
#
#     return distance
#
# def measure_distance_2(trig, echo):
#     trig.low()
#     time.sleep_us(2)
#     trig.high()
#     time.sleep_us(5)
#     trig.low()
#     while echo.value() == 0:
#         signal_off = time.ticks.us()
#     while echo.value() == 1:
#         signal_on = time.ticks_us()
#     time_passed = signal_on - signal_off
#     distance = (time_passed * 0.0343) / 2
#     return distance


#     def turn_90(self, left_or_right, speed=None):
#         if left_or_right == 'left':
#             self.motor_a.drive('backwards', speed)
#             self.motor_b.drive('forward', speed)
#             time.sleep(self.turn_duration_90)
#             self.stop_car()
#
#         elif left_or_right == 'right':
#             self.motor_a.drive('forward', speed)
#             self.motor_b.drive('backwards', speed)
#             time.sleep(self.turn_duration_90)
#             self.stop_car()
#
#         else:
#             print(f"\nInvalid left or right, speed or turn_duration in turn_90 method")
#
#
#     def turn_180(self, left_or_right):
#         if left_or_right == 'right':
#             self.turn_90('right', speed)
#             self.turn_90('right', speed)
#         elif left_or_right == 'left':
#             self.turn_90('left', speed)
#             self.turn_90('left', speed)
#


#     def measure_distance(self, print_interval=None):
#         current_time = time.time()
#
#         self.trig.value(1)
#         time.sleep_us(10)
#         self.trig.value(0)
#
#         while not self.echo.value():
#             pass
#         start = time.ticks_us()
#
#         while self.echo.value():
#             pass
#         end = time.ticks_us()
#
#         duration = time.ticks_diff(end, start)
#         distance = (duration * 0.0343) / 2
#         print(f"\nDistance: {distance}")
#         if print_interval is not None and (current_time - self.last_print_time) >= print_interval:
#             print(f"\nDistance: {distance}")
#             self.last_print_time = current_time
#
#         return distance
#


##################### Geymsla ####################

# Þessi leið er líka valid miðað við hvað ég les á netinu um þetta
# trig.value(0)
# time.sleep_us(2)
# trig.value(1)
# time.sleep_us(10)
# trig.value(0)


# Stilli Ultrasonic sensorinn
echo = Pin(47, Pin.IN)  # Pin(39, Pin.IN)
trig = Pin(48, Pin.OUT)  # Pin(38, Pin.OUT)


# Stilli Ultrasonic sensorinn
echo = Pin(39, Pin.IN)  # Pin(39, Pin.IN)
trig = Pin(38, Pin.OUT)  # Pin(38, Pin.OUT)
# Define Standby pin
stby = Pin(8, Pin.OUT)  # (STBY)

# Define pins for Motor A
# AIN1 = Pin(10, Pin.OUT)
# AIN2 = Pin(11, Pin.OUT)
# PWMA = PWM(Pin(17, Pin.OUT), 10000)


# Define pins for Motor B
# BIN1 = Pin(12, Pin.OUT)
# BIN2 = Pin(13, Pin.OUT)
# PWMB = PWM(Pin(16, Pin.OUT), 10000)


# Configure Pins for motor A
forward_pin_A = Pin(10, Pin.OUT)  # Motor A direction pin 1 (AIN1)
backward_pin_A = Pin(11, Pin.OUT)  # Motor A direction pin 2 (AIN2)
speed_pwm_A = PWM(Pin(17, Pin.OUT), freq=10000)  # Motor A speed control (PWMA)

# Configur Pins for motor B
forward_pin_B = Pin(12, Pin.OUT)  # Motor B direction pin 1 (BIN1)
backward_pin_B = Pin(13, Pin.OUT)  # Motor B direction pin 2 (BIN2)
speed_pwm_B = PWM(Pin(16, Pin.OUT), freq=10000)  # Motor B speed control (PWMB)


""" 
# ----- This is for better understanding and more easily written code ----- #
# --- I create more descriptive names from the pin setup for the coding --- #
motor_a_forward = AIN1
motor_a_backward = AIN2
motor_a_speed = PWMA

motor_b_forward = BIN1
motor_b_backward = BIN2
motor_b_speed = PWMB
 """


# --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- Motor A ----- --- --- --- #
# --- --- Forward - Backwards - Stop  --- --- #


def drive_motor_a_forward(a_speed):
    motor_a_forward.on()
    motor_a_backward.off()
    motor_a_speed.duty(a_speed)  # Adjust the speed


def drive_motor_a_backward(a_speed):
    motor_a_forward.off()
    motor_a_backward.on()
    motor_a_speed.duty(a_speed)  # Adjust the speed


def stop_motor_a():
    motor_a_forward.off()
    motor_a_backward.off()
    motor_a_speed.duty(0)


def stop_motor(motor):
    motor.forward.off()
    motor.backward.off()


# ------------------------------------------- #

# --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- Motor B ----- --- --- --- #
# --- --- Forward - Backwards - Stop  --- --- #
""" 
def drive_motor_b_forward(b_speed):
    motor_b_forward.on()
    motor_b_backward.off()
    motor_b_speed.duty(b_speed)  # Adjust the speed

def drive_motor_b_backward(b_speed):
    motor_b_forward.off()
    motor_b_backward.on()
    motor_b_speed.duty(b_speed)  # Adjust the speed

def stop_motor_b():
    motor_b_forward.off()
    motor_b_backward.off()
    motor_b_speed.duty(0)
 """
# ------------------------------------------- #


# --- --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- Motor A & B ----- --- --- --- #
# --- --- ---  Function for turning   --- --- --- #


# Functions for turning that takes time (turn_duration) to turn as
# argument so I can always change it
""" 
# Function for turning right
def turn_right(turn_duration):
    drive_motor_a_forward()
    drive_motor_b_backward()
    time.sleep(turn_duration)
    stop_motor_a()
    stop_motor_b()
    
# Function for turning left
def turn_left(turn_duration):
    drive_motor_a_backward()
    drive_motor_b_forward()
    time.sleep(turn_duration)
    stop_motor_a()
    stop_motor_b()
    

 """
""" 
# Here is another version of a turning function that takes "right" or "left" as arguments
# This function also takes the turn time as an argument
def turn(direction, turn_time=turn_duration):
    if direction == "right":
        drive_motor_a_forward(a_speed) # Adjustable from 1-1024 (512 half speed)
        drive_motor_b_backward(b_speed)
    elif direction == "left":
        drive_motor_a_backward(a_speed)
        drive_motor_b_forward(b_speed)
    time.sleep(turn_time)
    stop_motor_a()
    stop_motor_b()
    
     """
