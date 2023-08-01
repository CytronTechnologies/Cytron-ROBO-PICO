"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read distance from Ultrasonic Sensor HC-SR04P using MicroPython.

CONNECTION:
Robo Pico Grove 4 : HC-SR04P
GP16              - Echo
GP17              - Trig

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://microcontrollerslab.com/hc-sr04-ultrasonic-sensor-raspberry-pi-pico-micropython-tutorial/
"""
#Import necessary libraries
import time
from hcsr04 import HCSR04

#Define pin GP16 and GP17 used on the board
sonar = HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=10000)

while True:
    Distance = sonar.distance_cm()
    print('Distance : ', Distance, 'cm')
    time.sleep(1)
