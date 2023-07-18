"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read distance from Ultrasonic Sensor HC-SR04P using MicroPython

CONNECTION:
Robo Pico Maker Port : HC-SR04P
GP2                 - Echo
GP3                 - Trig

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-read-analog-sensor-value
"""
#Import necessary libraries
import time
from hcsr04 import HCSR04

#Define pin GP3 and GP2 used on the board
sonar = HCSR04(trigger_pin=3, echo_pin=2, echo_timeout_us=10000)

while True:
    Distance = sonar.distance_cm()
    print('Distance : ', Distance, 'cm')
    time.sleep(1)

