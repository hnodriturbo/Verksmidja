from machine import Pin, PWM
import time

# Set up PWM for the servo motor
servo = PWM(Pin(13), freq=50)  # Adjust pin number to your setup


# Function to move the servo
def move_servo(angle):
    # Convert angle to a PWM duty cycle (adjust the range as per your servo)
    duty = int((angle / 180) * 1023)
    servo.duty(duty)


# Move the mouth (or any other part) with the servo
while True:
    move_servo(90)  # Open mouth (midway)
    time.sleep(1)
    move_servo(0)  # Close mouth
    time.sleep(1)
    move_servo(180)  # Fully open mouth
    time.sleep(1)
