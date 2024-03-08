# ###########################################################
# ## ----------------- Hreiðar Pétursson ----------------- ##
# ## ----------------- Created March '24 ----------------- ##
# ###########################################################





# Dictionary holding configuration settings for the remote components
config = {
    "joystick": {
        "VRx_pin": 5,
        "VRy_pin": 6,
        "button_pin": 7
    },
    "lcd": {
        "lcd_i2c_address": 0x3F,
        "sda_pin": 40,
        "scl_pin": 39
    },
    # Add MPU settings if needed
    "mpu": {
        # Example settings, adjust as necessary
        "sda_pin": 21,
        "scl_pin": 22
    }
}