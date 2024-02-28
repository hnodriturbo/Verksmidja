# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## -------------- Created 10-20 February 2024 ---------- ##
# ###########################################################


# Basic imports
from machine import Pin, SoftI2C
import time


# Adjusted imports to reflect the new folder structure and content
from car_components_files.settings_functions import initialize_pins, toggle_logging, log_message
from car_components_files.motor_class import Motor
from car_components_files.car_class import Car
from car_components_files.addons import UltrasonicSensor, MPU6050


# To log to file set session_started to False and log_to_file to True
# Other way around to not log to file logfile.log
toggle_logging(True)

# Fetch and create the dictionary and inject it into the pins variable
pins = initialize_pins()

# Create Instances For Motor A & Motor B and set their default speed
motor_a = Motor(
    pins["forward_pin_A"],
    pins["backwards_pin_A"],
    pins["speed_pwm_A"],
    default_speed=672,  # This is approx correct straight direction
)
motor_b = Motor(
    pins["forward_pin_B"],
    pins["backwards_pin_B"],
    pins["speed_pwm_B"],
    default_speed=672,  # This is approx correct straight direction
)

# Create the standby settings variable from the dictionary
stby = pins["stby"]

# Set stby value to 1 - Ready to engage and log/print
stby.value(1)
log_message("stby value set to 1 (high)")

# Create UltraSonic Sensor Instance
ultrasonic_sensor = UltrasonicSensor(pins["trig"], pins["echo"])
log_message("Created the ultrasonic sensor instance")

log_message("Created the mpu instance")

# Create the car instance with motors, stby & ultrasonic sensor
car = Car(motor_a, motor_b, stby, ultrasonic_sensor) # missing mpu


while True:
    car.drive_car('forward', obstacle_detection=True)

    
