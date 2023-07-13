"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read distance from Ultrasonic Sensor HC-SR04P.

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
import board
import digitalio
import adafruit_hcsr04

#Define pin GP16 and GP17 used on the board
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP2)


def Read_Ultrasonic():
    time.sleep(0.1)
    return sonar.distance

while True:
    Distance = Read_Ultrasonic()
    print('Distance : ', Distance, 'cm')
    time.sleep(1)

