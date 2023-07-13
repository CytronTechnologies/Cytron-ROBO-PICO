"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up LEDs by pressing buttons on Robo Pico.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-press-the-buttons
"""
#import necessary libraries
import board
import digitalio
import time

#initialize leds on GP0 and GP1 pins
led1 = digitalio.DigitalInOut(board.GP0)
led2 = digitalio.DigitalInOut(board.GP1)

#set the led pins as output
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

#Initialize buttons on GP21 and GP20
btn1 = digitalio.DigitalInOut(board.GP20)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP21)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

while True:
    # Check button 1 (GP20) is pressed 
    if not btn1.value:
        #led1 is light up for 0.5s then turned off
        led1.value = True
        time.sleep(0.5)
        led1.value = False

    # Check button 2 (GP21) is pressed
    if not btn2.value: 
        #led2 is light up for 0.5s then turned off
        led2.value = True
        time.sleep(0.5)
        led2.value = False
