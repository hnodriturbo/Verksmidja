from machine import Pin, PWM
import time

# Motor A
ain1 = Pin(10, Pin.OUT)
ain2 = Pin(11, Pin.OUT)
pwma = PWM(Pin(17))

# Motor B
bin1 = Pin(12, Pin.OUT)
bin2 = Pin(13, Pin.OUT)
pwmb = PWM(Pin(16))

# Standby
stby = Pin(8, Pin.OUT)

# Initialize PWM
pwma.freq(1000)  # Set frequency for PWM
pwmb.freq(1000)

# Activate standby
stby.on()

def motor_a_forward(speed):
    ain1.on()
    ain2.off()
    pwma.duty(speed)

def motor_b_forward(speed):
    bin1.on()
    bin2.off()
    pwmb.duty(speed)

def stop_motors():
    ain1.off()
    ain2.off()
    bin1.off()
    bin2.off()
    pwma.duty(0)
    pwmb.duty(0)
    stby.off()  # Disable standby to stop the motors

# Example usage
motor_a_forward(512)  # Half speed forward
motor_b_forward(512)  # Half speed forward
time.sleep(2)
stop_motors()
