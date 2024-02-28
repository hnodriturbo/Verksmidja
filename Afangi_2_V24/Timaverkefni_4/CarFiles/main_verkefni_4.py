################################
## Last backup was 19feb 2024 ##
######### At time 20:55 ########


from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import (
    initialize_pins,
    Create_Car_Instance,
    UltrasonicSensor,
    Motor,
    Car,
    start_log_session,
)

# Fetch and create the dictionary and inject it into the pins variable
pins = initialize_pins()

# Let's create a instance we need to create the car instance using the pins from the dictionary
motor_a = Motor(
    pins["forward_pin_A"],
    pins["backwards_pin_A"],
    pins["speed_pwm_A"],
    default_speed=700,
)
motor_b = Motor(
    pins["forward_pin_B"],
    pins["backwards_pin_B"],
    pins["speed_pwm_B"],
    default_speed=672,
)
ultrasonic_sensor = UltrasonicSensor(pins["trig"], pins["echo"])

# Create the standby settings variable from the dictionary
stby = pins["stby"]

# Activate the car and make it ready to drive
stby.value(1)

# Create the car instance
car = Car(motor_a, motor_b, stby, ultrasonic_sensor)

start_log_session()
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
