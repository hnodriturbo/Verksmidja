from mpu6050 import MPU6050

mpu = MPU6050(sclpin=19, sdapin=21)  # Initialize with your actual pin numbers

# Optionally check the device ID or directly initialize the MPU6050
if mpu.mpu_init() == 0:  # Assuming you have an 'mpu_init' method
    print("MPU6050 initialized successfully.")

# Now you can read acceleration and gyroscope data
accel = mpu.get_acceleration()
gyro = mpu.get_gyroscope()
print(f"Acceleration: {accel}, Gyroscope: {gyro}")
