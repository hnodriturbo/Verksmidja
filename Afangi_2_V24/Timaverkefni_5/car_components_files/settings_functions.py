###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################

# This controls if the logs are logged to a file or not.
log_to_file = False

# This indicates whether the session has started, to control the initial logging behavior.
start_session = False


from machine import Pin, PWM
import time 


###########################################################
 ### ----- Functions for writing logs and print  ----- ###
###########################################################

def toggle_logging(value: bool):
    global log_to_file, start_session
    log_to_file = value
    # If enabling logging and the session has not started yet, mark the session as started.
    if value and not start_session:
        start_session = True
        log_message("Session started, logging enabled. \n")

def log_message(message, log_file_path="logfile.log"):
    global start_session
    
    # Log to file
    if log_to_file:
        
        if start_session:
            # Get the current time as a tuple
            current_time_tuple = time.localtime()
            
            # Format the time manually
            current_timestamp = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*current_time_tuple[0:6])
            
            # The start message
            start_message = f"\n\n\n\n\nCar Script Started - {current_timestamp}\n" \
                            "-----------------------------------------\n"
            
            with open(log_file_path, "a") as log_file:
                log_file.write(start_message)
            
            # Set the start_session to false after the initial log
            start_session = False
            
        # Log the message
        with open(log_file_path, "a") as log_file:
            log_file.write(message + "\n")
        print(message)
    else:
        # Print or handle differently if not logging to file
        print(message)


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
 ### ----- ----- Method To Initialize Pins ----- ----- ###
###########################################################
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
        # MPU6050 chip
        'mpu6050_sda': 45,
        'mpu6050_scl': 21,
        
        # NeoPixel Ring
        'neopixel_s' : Pin(4),
        'neopixel_num_leds': 8,
        
        # Buzzer
        'buzzer' : 35
    }
    return pins


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



        

