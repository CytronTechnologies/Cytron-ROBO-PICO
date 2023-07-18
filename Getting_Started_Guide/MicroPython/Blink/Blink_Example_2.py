"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up LEDs on Robo Pico using MicroPython

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-blink
"""
#import necessary libraries
from machine import Pin
import time

# Initialize led pins
LED = []
pins = [0, 1, 2, 3, 4, 5, 16, 17, 6, 26, 27, 7, 28]

for pin in pins:
    digout = Pin(pin, Pin.OUT)
    LED.append(digout)

while True:
    #Turn on LEDs one-by-one very quickly
    for i in range(len(pins)):
        LED[i].value(True)
        time.sleep(0.15)
        
    # Turn off LEDs one-by-one very quickly
    for i in range(len(pins)):
        LED[i].value(False)
        time.sleep(0.15)


