"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to play the tones using buzzer and press buttons on Robo Pico to play the tones
using MicroPython

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-turn-on-the-music
"""
#Import necessary libraries
from machine import Pin, PWM
import time

#Define the Melody Note and Duration
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

#Define pin connected to piezo buzzer
buzzer = PWM(Pin(22))

#Initialize buttons
btn1 = Pin(20, Pin.IN, Pin.PULL_UP)
btn2 = Pin(21, Pin.IN, Pin.PULL_UP)

#Play melody during start up  
for i in range(len(MELODY_DURATION)):
    #The board will not work with 0 frequency, so everytime the frequency is 0, it will rest for a duration of time
    if MELODY_NOTE[i] == 0:
        buzzer.duty_u16(0)  
    else:
        # Play melody tones
        buzzer.freq(MELODY_NOTE[i])
        buzzer.duty_u16(19660)
    time.sleep(MELODY_DURATION[i])
buzzer.duty_u16(0) #Turn off the buzzer

while True:
    # Check button (GP20) is pressed
    if not btn1.value():
        # Play tones
        # Format(pin,frequency,duration)
        buzzer.freq(262)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.freq(659)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.freq(784)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        
    # Check button (GP21) is pressed
    elif not btn2.value():
        # Play tones
        # Format(pin,frequency,duration)
        buzzer.freq(784)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.freq(659)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.freq(262)
        buzzer.duty_u16(19660)
        time.sleep(0.1)
        buzzer.duty_u16(0)