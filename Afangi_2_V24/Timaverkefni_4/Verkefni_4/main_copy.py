        #########################################
        ##### ----- Hreiðar Pétursson ----- #####
        ### -- Búið til 10-14 febrúar 2024 -- ###
        #########################################

# Backup up 18/2 2024 kl 17:00

from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import initialize_pins, UltrasonicSensor, Motor, Car
#from verkefni_4_settings_classes_functions import *

# Fetch and create the dictionary and inject it into the pins variable
pins = initialize_pins()

# Here I print out the keys and the values for show
for key, value in pins.items():
    print(f"\n{key} : {value}")


# For clarity - Motor A is left motor & Motor B is right motor


# Let's create a instance we need to create the car instance using the pins from the dictionary
motor_a = Motor(pins['forward_pin_A'], pins['backwards_pin_A'], pins['speed_pwm_A'], default_speed=625)
motor_b = Motor(pins['forward_pin_B'], pins['backwards_pin_B'], pins['speed_pwm_B'], default_speed=600)
ultrasonic_sensor = UltrasonicSensor(pins['trig'], pins['echo'])

##### ----- Motor A = 625 && Motor B = 600 ===== best straight path available ----- #####

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
    # Drive forward for 5 seconds (stop and continue to next code if distance < 50cm)
    obstacle_detected = myCar.drive_car('forward', 10)
    if obstacle_detected:
        print(f"\nStopped due to an obstacle.")
    else:
        print(f"\nStopped because timed out.")
    
    time.sleep(4)
    
    
    for _ in range(2):
        for _ in range(4):
            myCar.turn_90('left')
            time.sleep(2)
        for _ in range(4):
            myCar.turn_90('right')
            time.sleep(2)
        
    # 4x360° right and left circles
    for _ in range(4):
        myCar.turn_360('right')
        time.sleep(2)
        
    for _ in range(4):
        myCar.turn_360('left')
        time.sleep(2)


    print(f"\nEnd of loop.")    
    # Sleep for 10 seconds
    time.sleep(10)
    
  

















