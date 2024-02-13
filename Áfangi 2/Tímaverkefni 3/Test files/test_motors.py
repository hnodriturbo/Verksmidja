from machine import Pin, PWM
import time

# Define and set the motor A pin settings
motor_a_forward = Pin(10, Pin.OUT)
motor_a_backward = Pin(11, Pin.OUT)
motor_a_speed = PWM(Pin(17))

# Define and set the motor B pin settings
motor_b_forward = Pin(12, Pin.OUT)
motor_b_backward = Pin(13, Pin.OUT)
motor_b_speed = PWM(Pin(16))

# Initialize PWM - This only sets the frequency of response time of the motor - 1000 is normal Hz
motor_a_speed.freq(1000)
motor_b_speed.freq(1000)

# Define Standby pin
STBY = Pin(8, Pin.OUT)

# Enable the motor driver (take out of standby)
STBY.on()

# Function to drive Motor A forward
def drive_motor_a_forward():
    motor_a_forward.on()
    motor_a_backward.off()
    motor_a_speed.duty(512)  # 50% duty cycle, adjust as necessary for your motors

# Function to drive Motor A backward
def drive_motor_a_backward():
    motor_a_forward.off()
    motor_a_backward.on()
    motor_a_speed.duty(512)  # 50% duty cycle, adjust as necessary for your motors

# Function to stop Motor A
def stop_motor_a():
    motor_a_forward.off()
    motor_a_backward.off()
    motor_a_speed.duty(0)

# Function to drive Motor B forward
def drive_motor_b_forward():
    motor_b_forward.on()
    motor_b_backward.off()
    motor_b_speed.duty(512)  # 50% duty cycle, adjust as necessary for your motors

# Function to drive Motor B backward
def drive_motor_b_backward():
    motor_b_forward.off()
    motor_b_backward.on()
    motor_b_speed.duty(512)  # 50% duty cycle, adjust as necessary for your motors

# Function to stop Motor B
def stop_motor_b():
    motor_b_forward.off()
    motor_b_backward.off()
    motor_b_speed.duty(0)

# Test Motor A and B functions
# Call these functions one at a time to test each behavior
while True:
    drive_motor_a_forward()
    drive_motor_b_forward()
    time.sleep(2)
    stop_motor_a()
    stop_motor_b()

    time.sleep(2)

    drive_motor_a_backward()
    drive_motor_b_backward()
    time.sleep(2)
    stop_motor_a()
    stop_motor_b()
    
    time.sleep(2)

