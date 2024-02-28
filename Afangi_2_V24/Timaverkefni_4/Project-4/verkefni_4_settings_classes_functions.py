        #########################################
        ##### ----- Hreiðar Pétursson ----- #####
        ### -- Búið til 10-14 febrúar 2024 -- ###
        #########################################

from machine import Pin, PWM
import time 

# I decided to utilize and organize my code to make this a good and
# as much readable, reusable and understandable coding. Also for practise.


# Here i decided to use my coding skills for utilization and organize this into a dictionary
def initialize_pins():
    pins = {
        # Motor A
        'forward_pin_A': Pin(10, Pin.OUT),
        'backward_pin_A': Pin(11, Pin.OUT),
        'speed_pwm_A': PWM(Pin(17, Pin.OUT), freq=10000),
        # Motor B
        'forward_pin_B': Pin(12, Pin.OUT),
        'backward_pin_B': Pin(13, Pin.OUT),
        'speed_pwm_B': PWM(Pin(16, Pin.OUT), freq=10000),
        # Standby Pin
        'stby': Pin(8, Pin.OUT),
        # Ultrasonic Sensor
        'echo': Pin(39, Pin.IN),
        'trig': Pin(38, Pin.OUT),
    }
    return pins


# When I was finding out the right and same speed for both motors I
# found out that 430 for motor A was the same speed as 512 for motor B
a_speed = 430 # These two make up about the same speed
b_speed = 512 #             - || -

# Set the turn time (using speeds 430 and 512 makes this almost a 90° turn)
turn_duration = 0.4


# Fallið sem mælir vegalengd i sentimetrum
def measure_distance(trig, echo):
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    while not echo.value():
        pass
    start = time.ticks_us()

    while echo.value():
        pass
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    
    distance = (duration * 0.0343) / 2

    return distance

def measure_distance_2(trig, echo):
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    while echo.value() == 0:
        signal_off = time.ticks.us()
    while echo.value() == 1:
        signal_on = time.ticks_us()
    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2
    return distance


class Motor:
    def __init__(self, forward, backwards, speed_pwm, default_speed) -> None:
        self.forward = forward
        self.backwards = backwards
        self.speed_pwm = speed_pwm
        self.default_speed = default_speed
        
    def set_speed(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.speed_pwm.duty(speed)
    
    # Method for driving both forward and backwards
    def drive(self, direction, speed=None):
        # Drive motor forward
        if direction == 'forward':
            self.forward.value(1)
            self.backwards.value(0)
        # Drive Motor Backwards
        elif direction == 'backwards':
            self.forward.value(0)
            self.backwards.value(1)
        # In case of some errors
        else:
            print("Invalid Direction")
            return
        # Set the speed to the selected speed 
        # (if there is none speed value, then it reverts to the default speed)
        self.set_speed(speed)
    
    def stop(self):
        self.set_speed(0)


class Car:
    def __init__(self, motor_a, motor_b, stby_pin, ultrasonic_sensor):
        # Initialize motor objects with specific pins and PWM frequencies
        self.motor_a = motor_a
        self.motor_b = motor_b
        self.stby = stby_pin
        self.ultrasonic_sensor = ultrasonic_sensor
        
    # Drive forward for a specific period of time or constant until 50cm mark is reached 
    def drive_forward(self, duration=None, speed=None):
        self.motor_a.drive('forward', speed)
        self.motor_b.drive('forward', speed)
        if duration is not None:
            time.sleep(duration)
            self.motor_a.stop()
            self.motor_b.stop()
            return
        while True:
            
            distance = self.ultrasonic_sensor.measure_distance()
            if distance < 50:
                print("\nI measured a disance below 50cm or {distance} cm. Now stopping the car")
                self.stop_car()
                break
            time.sleep(1)
        
        
    # Drive backwards for a specific period of time or constant until 50cm mark is reached 
    def drive_backwards(self, duration=None, speed=None):
        self.motor_a.drive('backwards', speed)
        self.motor_b.drive('backwards', speed)
        if duration is not None:
            time.sleep(duration)
            self.stop_car()
            return
        while True:
            
            distance = self.ultrasonic_sensor.measure_distance()
            if distance < 50:
                print("\nI measured a disance below 50cm or {distance} cm. Now stopping the car")
                self.stop_car()
                break
            time.sleep(1)
        
        
    def stop_car(self):
        self.motor_a.stop()
        self.motor_b.stop()
        
        
    def turn_90(self, left_or_right, speed=None, turn_duration=0.4):
        if left_or_right == 'left':
            self.motor_a.drive('forward', speed)
            self.motor_b.drive('bakwards', speed)
            time.sleep(turn_duration)
            self.motor_a.stop()
            self.motor_b.stop()
        elif left_or_right == 'right':
            self.motor_a.drive('backwards', speed)
            self.motor_b.drive('forward', speed)
            time.sleep(turn_duration)
            self.motor_a.stop()
            self.motor_b.stop()
        else:
            print(f"\nInvalid left or right, speed or turn_duration in turn_90 method")

        
    def turn_180(self):
        self.turn_90('right', 0.8)
        
        
    # Example method in Car class to demonstrate functionality
    def show_car_status(self):
        print("\nCar Status:\n")
        print(f"\nMotor A Status: \nForward={self.motor_a.forward.value()}, \nBackwards={self.motor_a.backwards.value()}, \nSpeed={self.motor_a.speed_pwm.duty()}, \nDefault speed={self.motor_a.default_speed}")
        print(f"\n\nMotor B Status: \nForward={self.motor_b.forward.value()}, \nBackwards={self.motor_b.backwards.value()}, \nSpeed={self.motor_b.speed_pwm.duty()}, \nDefault speed={self.motor_b.default_speed}")
        # Add more status checks as needed

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin
        self.last_print_time = 0

    def measure_distance(self, print_interval=None):
        current_time = time.time()
        
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        
        while not self.echo.value():
            pass
        start = time.ticks_us()
        
        while self.echo.value():
            pass
        end = time.ticks_us()
        
        duration = time.ticks_diff(end, start)
        distance = (duration * 0.0343) / 2
        print(f"\nDistance: {distance}")
        if print_interval is not None and (current_time - self.last_print_time) >= print_interval:
            print(f"\nDistance: {distance}")
            self.last_print_time = current_time
        
        return distance
    






