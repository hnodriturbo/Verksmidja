###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################


from machine import Pin, PWM
import time 

from car_components_files.settings_functions import initialize_pins, log_message


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
        # Execute log/print of the initialization
        self.log_motor_status()
        # Make sure the motors are set to be stopped when created
        self.forward.value(0)
        self.backwards.value(0)
        
    # Log the motor's status once it's created
    def log_motor_status(self):
        parts = [
            "\nMotor Initialized: \n",
            f"Forward Pin={self.forward}, \n",
            f"Backwards Pin={self.backwards}, \n",
            f"Speed PWM={self.speed_pwm}, \n",
            f"Default Speed={self.default_speed}\n"
        ]
        
        message = "".join(parts)
        log_message(message)
    
    # Set the speed, if speed is None, revert to default
    def set_speed(self, speed=None):
        if speed is None:
            speed = self.default_speed
        speed = max(0, min(speed, 1023))
        self.speed_pwm.duty(int(speed))
        self.current_speed = speed
    
    # Return the value of the current speed
    def get_current_speed(self):
        return self.current_speed
    
    # Method for driving both forward and backwards
    def drive(self, direction, speed=None):
        # Forward
        if direction == 'forward':
            self.forward.value(1)
            self.backwards.value(0)
        # Backwards
        elif direction == 'backwards':
            self.forward.value(0)
            self.backwards.value(1)
        # Stop (currently not being used I think)
        elif direction == 'stop':
            self.stop()
        # In case of some errors
        else:
            log_message("Motor drive method: Invalid Direction")
            return 
        # (If speed is None, it reverts to the default speed)
        self.set_speed(speed)
    
    def stop(self):
        self.set_speed(0)

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
        
