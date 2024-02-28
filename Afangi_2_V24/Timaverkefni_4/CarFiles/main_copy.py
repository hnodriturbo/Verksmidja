###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################


from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import *

# Fetch and create the dictionary and inject it into the pins variable
pins = initialize_pins()

# Create Instances For Motor A & Motor B and set their default speed
motor_a = Motor(
    pins["forward_pin_A"],
    pins["backwards_pin_A"],
    pins["speed_pwm_A"],
    default_speed=700,  # Editable default speed for easier management
)
motor_b = Motor(
    pins["forward_pin_B"],
    pins["backwards_pin_B"],
    pins["speed_pwm_B"],
    default_speed=672,  # Editable default speed for easier management
)
ultrasonic_sensor = UltrasonicSensor(pins["trig"], pins["echo"])

# Create the standby settings variable from the dictionary
stby = pins["stby"]

# Activate the car and make it ready to drive
stby.value(1)
log_message(f"\nstby value set to 1 (high) = {stby.value()}")


# Log the motor's status once it's created
def log_motor_status(self):
    message = (
        f"\nMotor Initialized: \n"
        f"Forward Pin={self.forward}, \n"
        f"Backwards Pin={self.backwards}, \n"
        f"Speed PWM={self.speed_pwm}, \n"
        f"Default Speed={self.default_speed}"
    )
    log_message(message)


# Create the car instance
car = Car(motor_a, motor_b, stby, ultrasonic_sensor)
# log_message("\nCar Components Initialized:")
# log_message(
#     f"\nMotor A: \nForward Pin={motor_a.forward}, \nBackwards Pin={motor_a.backwards}, \nSpeed PWM={motor_a.speed_pwm}, \nDefault Speed={motor_a.default_speed}"
# )
# log_message(
#     f"\n\nMotor B: \nForward Pin={motor_b.forward}, \nBackwards Pin={motor_b.backwards}, \nSpeed PWM={motor_b.speed_pwm}, \nDefault Speed={motor_b.default_speed}"
# )
# log_message(f"\n\nStandby Pin: {stby}")


# Print the car status and log it
car.show_car_status()


while True:
    for x in range(4):
        car.turn_90("left")
        time.sleep(2)
    for x in range(4):
        car.turn_90("right")
        time.sleep(2)

    for x in range(4):
        car.turn_180("right")
        time.sleep(2)
    for x in range(4):
        car.turn_180("left")
        time.sleep(2)


# Start the log (I print into logs/logfile.log instead of printing directly. The log function also prints out messages)
start_log_session()
# Call obstacle detection with the car instance
# car.drive_car('forward', obstacle_detection=True)
