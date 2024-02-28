        #########################################
        ##### ----- Hreiðar Pétursson ----- #####
        ### -- Búið til 10-14 febrúar 2024 -- ###
        #########################################

from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import initialize_pins, UltrasonicSensor, Motor, Car
#from verkefni_4_settings_classes_functions import *

# Fetch and create the dictionary and inject it into the pins variable
pins = initialize_pins()

# Here I print out the keys and trhe values for show
for key, value in pins.items():
    print(f"\n{key} : {value}")

# Let's create a instance we need to create the car instance using the pins from the dictionary
motor_a = Motor(pins['forward_pin_A'], pins['backward_pin_A'], pins['speed_pwm_A'], default_speed=430)
motor_b = Motor(pins['forward_pin_B'], pins['backward_pin_B'], pins['speed_pwm_B'], default_speed=512)
ultrasonic_sensor = UltrasonicSensor(pins['trig'], pins['echo'])

# Create the standby settings variable from the dictionary
stby = pins['stby']

stby.value(1) # Activate the car and make it ready to drive
print(f"\nstby value set to 1 (high) = {stby.value}")
# Now print details of each motor and the standby pin to make sure everything was created correctly
print("\nCar Components Initialized:")
print(f"\nMotor A: \nForward Pin={motor_a.forward}, \nBackwards Pin={motor_a.backwards}, \nSpeed PWM={motor_a.speed_pwm}, \nDefault Speed={motor_a.default_speed}")
print(f"\n\nMotor B: \nForward Pin={motor_b.forward}, \nBackwards Pin={motor_b.backwards}, \nSpeed PWM={motor_b.speed_pwm}, \nDefault Speed={motor_b.default_speed}")
print(f"\n\nStandby Pin: {stby}")

myCar = Car(motor_a, motor_b, stby, ultrasonic_sensor)




# Call the method to print status
myCar.show_car_status()





while True:
    # Drive forward continuously
    myCar.drive_forward()
    
    
    myCar.turn_180()
    
    time.sleep(2)
    












