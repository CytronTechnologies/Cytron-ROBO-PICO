"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the servo on the Robo Pico servo port using MicroPython.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
"""
import time
from machine import Pin, PWM

# create a PWMOut object on the control pin.
pwm1 = PWM(Pin(12))
pwm2 = PWM(Pin(13))
pwm3 = PWM(Pin(14))
pwm4 = PWM(Pin(15))
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

# You might need to calibrate the min_dutycycle (pulse at 0 degrees) and max_dutycycle (pulse at 180 degrees) to get an accurate servo angle.
# The servo dutycycle values 2200-8300 represent 0-180 degrees.
angle = 0.0
min_dutycycle = 2200
max_dutycycle = 8300
dutycycle = 0

while True:
    #Set servo angle
    angle = 180
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Update servo angles.
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    # Change the angle every 1 second.
    time.sleep(1)

    #Set servo angle
    angle = 0
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Update servo angles.
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    # Change the angle every 1 second.
    time.sleep(1)
