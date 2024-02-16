
    
    
    
    
    
##################### Geymsla ####################
    
    # Þessi leið er líka valid miðað við hvað ég les á netinu um þetta
    #trig.value(0)
    #time.sleep_us(2)
    #trig.value(1)
    #time.sleep_us(10)
    #trig.value(0)


# Stilli Ultrasonic sensorinn
echo = Pin(47, Pin.IN) # Pin(39, Pin.IN)
trig = Pin(48, Pin.OUT) # Pin(38, Pin.OUT)


# Stilli Ultrasonic sensorinn
echo = Pin(39, Pin.IN) # Pin(39, Pin.IN)
trig = Pin(38, Pin.OUT) # Pin(38, Pin.OUT)
# Define Standby pin
stby = Pin(8, Pin.OUT) # (STBY)

# Define pins for Motor A
# AIN1 = Pin(10, Pin.OUT)  
# AIN2 = Pin(11, Pin.OUT)  
# PWMA = PWM(Pin(17, Pin.OUT), 10000)  


# Define pins for Motor B
# BIN1 = Pin(12, Pin.OUT)  
# BIN2 = Pin(13, Pin.OUT)  
# PWMB = PWM(Pin(16, Pin.OUT), 10000)  


    

# Configure Pins for motor A
forward_pin_A = Pin(10, Pin.OUT) # Motor A direction pin 1 (AIN1)
backward_pin_A = Pin(11, Pin.OUT) # Motor A direction pin 2 (AIN2)
speed_pwm_A = PWM(Pin(17, Pin.OUT), freq=10000) # Motor A speed control (PWMA)

# Configur Pins for motor B
forward_pin_B = Pin(12, Pin.OUT) # Motor B direction pin 1 (BIN1)
backward_pin_B = Pin(13, Pin.OUT) # Motor B direction pin 2 (BIN2)
speed_pwm_B = PWM(Pin(16, Pin.OUT), freq=10000) # Motor B speed control (PWMB)







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
