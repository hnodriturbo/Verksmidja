import machine
import time

# Motor initialization
forward_pin_A = Pin(10, Pin.OUT)
backward_pin_A = Pin(11, Pin.OUT)
speed_pwm_A = PWM(Pin(17, Pin.OUT), freq=10000)

forward_pin_B = Pin(12, Pin.OUT)
backward_pin_B = Pin(13, Pin.OUT)
speed_pwm_B = PWM(Pin(16, Pin.OUT), freq=10000)

# Function to control motor
def control_motor(forward, backward, speed_pwm, direction, duration, speed=1000):
    if direction == 'forward':
        forward.value(1)
        backward.value(0)
    elif direction == 'backward':
        forward.value(0)
        backward.value(1)
    else:
        print("Invalid direction")
        return
    
    speed_pwm.duty(speed)
    time.sleep(duration)
    speed_pwm.duty(0)  # Stop the motor
    forward.value(0)
    backward.value(0)
while True:
    # Test Motor A
    print("Testing Motor A - Forward")
    control_motor(forward_pin_A, backward_pin_A, speed_pwm_A, 'forward', 3)
    time.sleep(1)  # Wait for a second before next test

    print("Testing Motor A - Backward")
    control_motor(forward_pin_A, backward_pin_A, speed_pwm_A, 'backward', 3)
    time.sleep(1)

    # Test Motor B
    print("Testing Motor B - Forward")
    control_motor(forward_pin_B, backward_pin_B, speed_pwm_B, 'forward', 3)
    time.sleep(1)

    print("Testing Motor B - Backward")
    control_motor(forward_pin_B, backward_pin_B, speed_pwm_B, 'backward', 3)
