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
