"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up LEDs on Robo Pico.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-blink
"""
#import necessary libraries
import board
import digitalio
import time

# Initialize led pins
LED = []
pins = [board.GP0, board.GP1,board.GP2, board.GP3, board.GP4, board.GP5, board.GP16, board.GP17, board.GP6, board.GP26, board.GP27, board.GP7, board.GP28]

for pin in pins:
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LED.append(digout)

while True:
    #Turn on LEDs one-by-one very quickly
    for i in range(len(pins)):
        LED[i].value = True
        time.sleep(0.15)
        
    # Turn off LEDs one-by-one very quickly
    for i in range(len(pins)):
        LED[i].value = False
        time.sleep(0.15)
