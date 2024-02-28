###########################################################
## ----------------- Hreiðar Pétursson ----------------- ##
## -------------- Created 10-20 February 2024 ---------- ##
###########################################################

from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import *

try:
    # Fetch and create the dictionary and inject it into the pins variable
    pins = initialize_pins()

    # Start the log/print
    start_log_session()

    # Create Instances For Motor A & Motor B and set their default speed
    motor_a = Motor(
        pins["forward_pin_A"],
        pins["backwards_pin_A"],
        pins["speed_pwm_A"],
        default_speed=700,  # This is approx correct straight direction
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

    # Create the car instance with motors, stby & ultrasonic sensor
    car = Car(motor_a, motor_b, stby, ultrasonic_sensor)

    # Call obstacle detection with the car instance
    car.drive_car('forward', obstacle_detection=True)

except Exception as e:
    log_message(f"Error encountered: {e}")