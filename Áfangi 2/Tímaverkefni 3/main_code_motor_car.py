#########################################
##### ----- Hreiðar Pétursson ----- #####
### ---- Búið til 30 janúar 2024 ---- ###
#########################################

from machine import Pin, PWM
import time 





# Define pins for Motor A
AIN1 = Pin(10, Pin.OUT)  # Motor A direction pin 1
AIN2 = Pin(11, Pin.OUT)  # Motor A direction pin 2
PWMA = PWM(Pin(17, Pin.OUT), 10000)  # Motor A speed control

# Define pins for Motor B
BIN1 = Pin(12, Pin.OUT)  # Motor B direction pin 1
BIN2 = Pin(13, Pin.OUT)  # Motor B direction pin 2
PWMB = PWM(Pin(16, Pin.OUT), 10000)  # Motor B speed control

# Define Standby pin
STBY = Pin(8, Pin.OUT)

# When I was finding out the right and same speed for both motors I
# found out that 430 for motor A was the same speed as 512 for motor B
a_speed = 430
b_speed = 512
# Set the turn time (using speeds 430 and 512 makes this almost a 90° turn)
turn_duration = 0.5






# ----- This is for better understanding and more easily written code ----- #
# --- I create more descriptive names from the pin setup for the coding --- #
motor_a_forward = AIN1
motor_a_backward = AIN2
motor_a_speed = PWMA

motor_b_forward = BIN1
motor_b_backward = BIN2
motor_b_speed = PWMB






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
    
# ------------------------------------------- #

# --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- Motor B ----- --- --- --- #
# --- --- Forward - Backwards - Stop  --- --- #

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

# ------------------------------------------- #



# --- --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- Motor A & B ----- --- --- --- #
# --- --- ---  Function for turning   --- --- --- #

# Functions for turning that takes time (turn_duration) to turn as
# argument so I can always change it

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
    
    


# --- --- --- --- --- --- --- --- --- --- --- #
# --- --- --- ----- My Code ----- --- --- --- #
# --- -- -- Running code on startup -- -- --- #


# Enable the motor driver (take out of standby)
STBY.on()

while True:
    # Drive forward at speed 1000 for 1 second
    drive_motor_a_forward(1000)
    drive_motor_b_forward(1000)
    time.sleep(1)
    stop_motor_a()
    stop_motor_b()

    # Stop for 0.5 seconds
    time.sleep(0.5)

    # Turn right (90°)
    turn("right", turn_duration)
    # turn_right(turn_duration)
    
    # Wait half a second
    time.sleep(0.5)

    # Drive forward at speed 700 for 1 second
    drive_motor_a_forward(700)
    drive_motor_b_forward(700)
    time.sleep(1)
    stop_motor_a()
    stop_motor_b()

    # Wait half a second
    time.sleep(0.5)

    # Turn right (90°)
    # turn_right(turn_duration)
    turn("right", turn_duration)
    time.sleep(0.5)

    # Drive forward at speed 1000 for 1 second
    drive_motor_a_forward(1000)
    drive_motor_b_forward(1000)
    time.sleep(1)
    stop_motor_a()
    stop_motor_b()

    # Stop for 0.5 seconds
    time.sleep(0.5)

    # Turn left (90°)
    # turn_left(turn_duration)
    turn("left", turn_duration)
    time.sleep(0.5)

    # Drive backward at speed 700 for 1 second
    drive_motor_a_backward(700)
    drive_motor_b_backward(700)
    time.sleep(1)
    stop_motor_a()
    stop_motor_b()

    # Stop for 0.5 seconds
    time.sleep(0.5)

    # Turn left (90°)
    # turn_left(turn_duration)
    turn("left", turn_duration)
    time.sleep(0.5)

    # This loop will repeat these actions indefinitely

