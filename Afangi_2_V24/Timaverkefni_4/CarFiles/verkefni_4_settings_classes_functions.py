#########################################
##### ----- Hreiðar Pétursson ----- #####
### -- Búið til 10-14 febrúar 2024 -- ###
#########################################

from machine import Pin, PWM
import time

# I decided to utilize and organize my code to make this a good and
# as much readable, reusable and understandable coding. Also for practise.


def Create_Car_Instance():

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
        default_speed=660,
    )
    ultrasonic_sensor = UltrasonicSensor(pins["trig"], pins["echo"])

    # Create the standby settings variable from the dictionary
    stby = pins["stby"]

    stby.value(1)  # Activate the car and make it ready to drive

    myCar = Car(motor_a, motor_b, stby, ultrasonic_sensor)

    return myCar, ultrasonic_sensor


# Here i decided to use my coding skills for utilization and organize this into a dictionary
def initialize_pins():
    pins = {
        # Motor A
        "forward_pin_A": Pin(11, Pin.OUT),
        "backwards_pin_A": Pin(10, Pin.OUT),
        "speed_pwm_A": PWM(Pin(17, Pin.OUT), freq=10000),
        # Motor B
        "forward_pin_B": Pin(13, Pin.OUT),
        "backwards_pin_B": Pin(12, Pin.OUT),
        "speed_pwm_B": PWM(Pin(16, Pin.OUT), freq=10000),
        # Standby Pin
        "stby": Pin(8, Pin.OUT),
        # Ultrasonic Sensor
        "echo": Pin(39, Pin.IN),
        "trig": Pin(38, Pin.OUT),
    }
    return pins


###########################################################
#### ----- ----- Motor Class And Methods ----- ----- ####
###########################################################


class Motor:
    def __init__(self, forward, backwards, speed_pwm, default_speed) -> None:
        self.forward = forward
        self.backwards = backwards
        self.speed_pwm = speed_pwm
        self.default_speed = default_speed
        self.current_speed = default_speed

    def set_speed(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.speed_pwm.duty(int(speed))
        self.current_speed = speed

    def get_current_speed(self):
        return self.current_speed

    # Method for driving both forward and backwards
    def drive(self, direction, speed=None):
        # Drive motor forward
        if direction == "forward":
            self.forward.value(1)
            self.backwards.value(0)
        # Drive Motor Backwards
        elif direction == "backwards":
            self.forward.value(0)
            self.backwards.value(1)
        elif direction == "stop":
            self.stop()
        # In case of some errors
        else:
            print("Invalid Direction")
            return
        # Set the speed to the selected speed
        # (if there is none speed value, then it reverts to the default speed)
        self.set_speed(speed)

    def stop(self):
        self.set_speed(0)


###########################################################
###########################################################


###########################################################
##### ----- ----- Car Class And Methods ----- ----- #####
###########################################################


class Car:
    def __init__(self, motor_a, motor_b, stby_pin, ultrasonic_sensor):

        # Initialize motor objects with specific pins and PWM frequencies
        self.motor_a = motor_a
        self.motor_b = motor_b

        # Initialize Standby Pin
        self.stby = stby_pin

        # Initialize The UltraSonic Sensor
        self.ultrasonic_sensor = ultrasonic_sensor

        # Extra properties
        self.turn_speed_left_a = 0
        self.turn_speed_left_b = 475

        self.turn_speed_right_a = 520
        self.turn_speed_right_b = 0

        self.turn_duration_90 = 0.7
        self.turn_duration_180 = (2 * self.turn_duration_90) - 0.1
        self.turn_duration_270 = 3 * self.turn_duration_90
        self.turn_duration_360 = 4 * self.turn_duration_90

        ############################################
        ##### ----- Drive & Stop Methods ----- #####
        ############################################

    # This way, the car drives and has a obstacle detection to true or false

    def drive_car(self, direction, duration=None, speed=None, obstacle_detection=False):
        # Record the start time
        start_time = time.time()

        # Start Driving
        self.motor_a.drive(direction, speed)
        self.motor_b.drive(direction, speed)
        log_message(
            f"Started driving in direction: {direction} and with speed: Motor A: {self.motor_a.get_current_speed()} Motor B: {self.motor_b.get_current_speed()}"
        )

        # If obstacle_detection is True and no duration
        if obstacle_detection and not duration:
            # Proceed in chosen direction

            while True:
                distance = self.ultrasonic_sensor.measure_distance()
                log_message(f"\nMeasured Distance: {distance}")
                if distance < 50:
                    # Stop and back up slightly
                    self.stop_car()
                    time.sleep(2)  # Wait for 1 second to simulate backing up

                    # Turn left 90 degrees and measure distance
                    self.turn_90("right")
                    distance_right = self.ultrasonic_sensor.measure_distance()
                    log_message(f"Measured distance to the right: {distance_right}")
                    time.sleep(2)

                    # Turn 180 degrees to the right (totaling 270 from original direction) and measure distance
                    self.turn_180("right")
                    distance_left = self.ultrasonic_sensor.measure_distance()
                    log_message(f"Measured distance to the left: {distance_left}")
                    time.sleep(2)

                    # Compare distances and choose direction with more clearance
                    log_message(f"Comparing distances and choosing direction")
                    if distance_left >= distance_right and distance_left > 50:
                        # No need to turn as car is already facing the direction with more clearance
                        log_message(
                            f"Distance left is more then distance right and more then 50cm. Continue to the left direction"
                        )
                        pass
                    elif distance_right >= distance_left and distance_right > 50:
                        log_message(
                            f"Distance right is more then distance left and more then 50cm. Turning back to left direction"
                        )
                        self.turn_180("right")  # Turn back to the left direction
                    else:
                        # If no clear path or both < 50cm, turn 90° more to the right, to face the back direction
                        log_message(f"Both ways less then 50cm")
                        self.turn_90("left")
                    # Wait 2 seconds before resuming driving or turning again
                    time.sleep(2)

                    # After handling obstacle, resume driving
                    self.motor_a.drive(direction, speed)
                    self.motor_b.drive(direction, speed)

                time.sleep(0.2)

        elif duration:
            time.sleep(duration)
            self.stop_car()

        else:
            log_message(
                f"You need to specify either obstacle detection as True and no duration or specify duration"
            )

    def stop_car(self):
        self.motor_a.stop()
        self.motor_b.stop()
        log_message(f"\nstop_car method called")

        #######################################
        ##### ----- Turning Methods ----- #####
        #######################################

    def turn(self, left_or_right):
        # Turn right with motor A
        if left_or_right == "right":
            self.motor_a.drive("forward", self.turn_speed_right_a)
            self.motor_b.stop()
        # Turn left with Motor B
        else:
            self.motor_b.drive("forward", self.turn_speed_left_b)
            self.motor_a.stop()

        log_message(f"\nTurning {left_or_right}.")

        # Stop the other motor
        # (self.motor_b if left_or_right == 'right' else self.motor_a).stop()

    # Method for turning 90°
    def turn_90(self, left_or_right):
        # Execute turn
        self.turn(left_or_right)
        # Turning
        time.sleep(self.turn_duration_90)
        # Stop car
        self.stop_car()
        # Print out completetion of turning
        log_message(f"\nCompleted 90° turn to the {left_or_right}.")

    # For 180° turns
    def turn_180(self, left_or_right):
        self.turn(left_or_right)
        time.sleep(self.turn_duration_180)
        self.stop_car()
        log_message(f"\nCompleted 180° turn to the {left_or_right}.")

    # For 360° circle turning
    def turn_360(self, left_or_right):
        self.turn(left_or_right)
        time.sleep(self.turn_duration_360)
        self.stop_car()
        log_message(f"\nCompleted 360° turn to the {left_or_right}.")

    # Example method in Car class to demonstrate functionality
    def show_car_status(self):
        log_message("\nCar Status:\n")
        log_message(
            f"\nMotor A Status: \nForward={self.motor_a.forward.value()}, \nBackwards={self.motor_a.backwards.value()}, \nSpeed={self.motor_a.speed_pwm.duty()}, \nDefault speed={self.motor_a.default_speed}"
        )
        log_message(
            f"\n\nMotor B Status: \nForward={self.motor_b.forward.value()}, \nBackwards={self.motor_b.backwards.value()}, \nSpeed={self.motor_b.speed_pwm.duty()}, \nDefault speed={self.motor_b.default_speed}"
        )


###########################################################


def start_log_session():
    # Get the current time as a tuple
    current_time_tuple = (
        time.localtime()
    )  # Returns (year, month, day, hour, minute, second, weekday, yearday)

    # Format the time manually
    current_timestamp = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        *current_time_tuple[0:6]
    )

    start_message = (
        f"\n\n\n\n\nCar Script Started - {current_timestamp}\n"
        "-----------------------------------------\n"
    )

    with open("/logs/logfile.log", "a") as log_file:
        log_file.write(start_message)


def log_message(message):
    with open("/logs/logfile.log", "a") as log_file:
        log_file.write(message + "\n")
    print(message)


###########################################################
#### ----- Ultrasonic Sensor Class And Methods ----- ####
###########################################################


class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin

    def measure_distance(self):
        # Trigger the measurement
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        # Wait for the echo to start
        while not self.echo.value():
            pass
        start = time.ticks_us()

        # Wait for the echo to end
        while self.echo.value():
            pass
        end = time.ticks_us()

        # Calculate the duration and distance
        duration = time.ticks_diff(end, start)
        distance = (duration * 0.0343) / 2  # Convert time to distance

        return distance
