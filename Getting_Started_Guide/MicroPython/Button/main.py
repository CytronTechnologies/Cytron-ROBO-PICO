"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up LEDs by pressing buttons on Robo Pico using MicroPython.

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

#Initialize buttons on GP21 and GP20
btn1 = Pin(20, Pin.IN, Pin.PULL_UP)
btn2 = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    # Check button 1 (GP20) is pressed 
    if not btn1.value():
        #led1 is light up for 0.5s then turned off
        led1.value(True)
        time.sleep(0.5)
        led1.value(False)

    # Check button 2 (GP21) is pressed
    if not btn2.value(): 
        #led2 is light up for 0.5s then turned off
        led2.value(True)
        time.sleep(0.5)
        led2.value(False)
