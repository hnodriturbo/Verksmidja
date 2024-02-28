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


try:
    # Fetch and create the dictionary and inject it into the pins variable
    pins = initialize_pins()

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




# scl_pin = 45  # SCL pin
# sda_pin = 21  # SDA pin



# Fetch and create the dictionary and inject it into the pins variable
# pins = initialize_pins()


# Setup I2C
scl_pin = pins['mpu6050_scl']
sda_pin = pins['mpu6050_sda']


i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))


# Scan for devices and print the address or the device
devices = i2c.scan()
print("I2C devices found:", devices)


mpu = MPU6050(scl_pin, sda_pin)  # Modify the GPIOs as required in your context


# Reading the sensor for only Yaw is one angle, assuming your car's flat and moving only on the z-axis.
# A general utilization might rely on a PID to handle sensor's report to re-steer your car.
while True:
    ax, ay, az = mpu.get_accel_data()
    # Note: ax, ay, and az return as proportional rates to g (9.81 m/s²).
    # e.g., checking for movement along the car's intended right
    print(f"Acceleration X: {ax}, Y: {ay}, Z: {az}")
    time.sleep(1)

