"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up LEDs on Robo Pico using MicroPython.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
"""
#import necessary libraries
from machine import Pin
import time

#initialize leds on GP0 and GP1 pins as output
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)

while True:
    #led1 is light up for 0.5s then turned off
    led1.value(True)
    time.sleep(0.5)
    led1.value(False)
    time.sleep(0.5)

    #led2 is light up for 0.5s then turned off
    led2.value(True)
    time.sleep(0.5)
    led2.value(False)
    time.sleep(0.5)

