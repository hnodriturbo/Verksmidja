
from machine import Pin, PWM
import time
from verkefni_4_settings_classes_functions import Car, UltrasonicSensor

# Initialize the ultrasonic sensor and car with predefined settings
ultrasonic = UltrasonicSensor(trig_pin=Pin(38, Pin.OUT), echo_pin=Pin(39, Pin.IN))
car = Car()

def detect_obstacle_and_navigate():
    while True:
        distance = ultrasonic.measure_distance()
        if distance < 50:
            # Stop and back up slightly
            car.stop_car()
            time.sleep(1)  # Wait for 1 second to simulate backing up
            
            # Turn left 90 degrees and measure distance
            car.turn_90('left')
            distance_left = ultrasonic.measure_distance()
            
            # Turn 180 degrees to the right (totaling 270 from original direction) and measure distance
            car.turn_180('right')
            distance_right = ultrasonic.measure_distance()
            
            # Compare distances and choose direction with more clearance
            if distance_left > 50 and distance_left >= distance_right:
                car.turn_90('left')  # Turn back to the left direction
            elif distance_right > 50:
                # No need to turn as car is already facing the direction with more clearance
                pass
            else:
                # If no clear path, turn 180 degrees to face original direction
                car.turn_180('left')
            
            # Proceed in chosen direction
            car.drive_car('forward', duration=None, speed=None)
        else:
            car.drive_car('forward', duration=None, speed=None)

if __name__ == "__main__":
    detect_obstacle_and_navigate()
