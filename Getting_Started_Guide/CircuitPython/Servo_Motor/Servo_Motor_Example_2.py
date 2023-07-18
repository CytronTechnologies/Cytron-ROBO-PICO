"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the servo on the Robo Pico servo port.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-micro-servo-motor
"""
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

# create a PWMOut object on the control pin.
pwm1 = pwmio.PWMOut(board.GP12, duty_cycle=0, frequency=50)
pwm2 = pwmio.PWMOut(board.GP13, duty_cycle=0, frequency=50)
pwm3 = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)
pwm4 = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)

# You might need to calibrate the min_pulse (pulse at 0 degrees) and max_pulse (pulse at 180 degrees) to get an accurate servo angle.
# The pulse range is 750 - 2250 by default (if not defined).
# Initialize Servo objects.
servo1 = servo.Servo(pwm1, min_pulse=580, max_pulse=2700)
servo2 = servo.Servo(pwm2, min_pulse=580, max_pulse=2700)
servo3 = servo.Servo(pwm3, min_pulse=580, max_pulse=2700)
servo4 = servo.Servo(pwm4, min_pulse=580, max_pulse=2700)
angle = 0
add_angle = True

while True:
    # Condition to add angle
    if angle <= 0:
        add_angle = True
    if angle >= 180:
        add_angle = False
        
    # Add angle increment or decrement    
    if add_angle:
        angle += 5
    else:
        angle -= 5

    # Update servo angles.
    servo1.angle = servo2.angle = servo3.angle = servo4.angle = angle
    print("turn servo", angle)
    # Change the angle every 0.5 second.
    time.sleep(0.5)
