"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the servo on the Robo Pico servo port.

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
    
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Update servo angles.
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    print("turn servo", angle)
    # Change the angle every 0.5 second.
    time.sleep(0.5)
