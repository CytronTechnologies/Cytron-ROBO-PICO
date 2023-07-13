"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to play the tones using buzzer and press buttons on Robo Pico to play the tones.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-turn-on-the-music
"""
#Import necessary libraries
import board
import digitalio
import simpleio
import time

#Define the Melody Note and Duration
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

#Define pin connected to piezo buzzer
PIEZO_PIN = board.GP22

#Initialize buttons
btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP

#Play melody during start up  
for i in range(len(MELODY_DURATION)):
    #The boad will not work with 0 frequency, so everytime the frequency is 0, it will rest for a duration of time
    if MELODY_NOTE[i] == 0:
        time.sleep(MELODY_DURATION[i])
    else:
        # Play melody tones
        simpleio.tone(PIEZO_PIN, MELODY_NOTE[i], duration=MELODY_DURATION[i])

while True:
    # Check button (GP20) is pressed
    if not btn1.value:
        # Play tones
        # Format(pin,frequency,duration)
        simpleio.tone(PIEZO_PIN, 262, duration=0.1)
        simpleio.tone(PIEZO_PIN, 659, duration=0.15)
        simpleio.tone(PIEZO_PIN, 784, duration=0.2)
        
    # Check button (GP21) is pressed
    elif not btn2.value:
        # Play tones
        # Format(pin,frequency,duration)
        simpleio.tone(PIEZO_PIN, 784, duration=0.2)
        simpleio.tone(PIEZO_PIN, 659, duration=0.15)
        simpleio.tone(PIEZO_PIN, 262, duration=0.1)