# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## -------------- Created 10-20 February 2024 ---------- ##
# ###########################################################


# Basic imports
###############################################################
from machine import Pin, SoftI2C, I2C
import time
import _thread
###############################################################

# Imports from files
###############################################################
from car_components_files.settings_functions import initialize_pins, toggle_logging, log_message
from car_components_files.motor_class import Motor
from car_components_files.car_class import Car
from car_components_files.addons import UltrasonicSensor, NeoPixelRing, Buzzer 
from car_components_files.mpu6050_files.mpu6050_vector3d.imu import MPU6050
###############################################################

# To log to file set session_started to False and log_to_file to True
# Other way around to not log to file logfile.log
###############################################################
toggle_logging(False)
###############################################################


###############################################################
############## ---------- KENNARI ------------ ################

### EF ÞÚ VILT KVEIKJA Á LÖGGULJÓSUNUM ÞÁ BREYTIRU ÞESSU Í TRUE
use_cop_lights_flag = False  # Set to False for normal car lights




# Get the pins dictionary which holds all pins
###############################################################
pins = initialize_pins()
###############################################################





# Create the standby settings variable from the dictionary
###############################################################
stby = pins["stby"]
# Set stby value to 0 - Car Stopped
stby.value(0)
log_message("stby value set to 1 (high)")
###############################################################




# Create Instances For Motor A & Motor B, set default speed
###############################################################
motor_a = Motor(
    pins["forward_pin_A"],
    pins["backwards_pin_A"],
    pins["speed_pwm_A"],
    default_speed=725,  # This is approx correct straight direction
)
motor_a.forward(0)
motor_b = Motor(
    pins["forward_pin_B"],
    pins["backwards_pin_B"],
    pins["speed_pwm_B"],
    default_speed=700,  # This is approx correct straight direction
)
motor_b.forward(0)
###############################################################


# Create UltraSonic Sensor Instance
###############################################################
ultrasonic_sensor = UltrasonicSensor(pins["trig"], pins["echo"])
log_message("UltraSonicSensor instance created !")
###############################################################



# Create NeoPixel Instance
###############################################################

neopixel = NeoPixelRing(pins['neopixel_s'], pins['neopixel_num_leds'])
log_message("neo_pixel_ring instance created !")

###############################################################




# Buzzer Instance
###############################################################

# Create the Buzzer instance
buzzer = Buzzer(pins['buzzer'])
# Log message that the buzzer instance has been created and cop sounds are playing
log_message("Buzzer instance created !")
###############################################################



# Create the mpu instance
###############################################################
scl_pin = pins['mpu6050_scl']
sda_pin = pins['mpu6050_sda']

# Create an I2C instance
i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

# Initialize MPU6050 - Create the instance correctly with the I2C object
mpu = MPU6050(i2c)

####### CAR MUST BE IN STILL POSITION WHILE CALIBRATING !!!!! #####

# Calibrate the gyro (get 100 samples and use the center to calibrate)
mpu.calibrate_gyro()

###############################################################



################# Create the Car Instance #####################

# Create the car instance with motors, stby & ultrasonic sensor
car = Car(motor_a, motor_b, stby, ultrasonic_sensor, neopixel, mpu, buzzer, use_cop_lights=use_cop_lights_flag)

###############################################################



###############################################################
# 
# # Flag to control speed adjustment
# enable_speed_adjustment = True
# 
# if enable_speed_adjustment:
#     car.start_adjust_speed_thread()
# else:
#     car.stop_adjust_speed_thread()
#     
###############################################################





# Make car ready to drive
###############################################################
stby.value(1)
###############################################################




############# Drive car with obstacle detection ###############

# Call obstacle detection with the car instance
car.drive_car('forward', obstacle_detection=True)

###############################################################


#############          Turn Practising          ###############
# 
# while True:
#     for _ in range(4):
#         car.turn_180('left')
#         time.sleep(2)
#     for _ in range(4):
#         car.turn_180('right')
#         time.sleep(2)
#     for _ in range(4):
#         car.turn_90('left')
#         time.sleep(2)
#     for _ in range(4):
#         car.turn_90('right')
#         time.sleep(2)
# 
###############################################################

