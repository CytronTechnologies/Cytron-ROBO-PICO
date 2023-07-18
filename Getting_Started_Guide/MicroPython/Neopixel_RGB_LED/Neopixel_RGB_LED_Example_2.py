"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up neopixel rgb led on Robo Pico using MicroPython.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpyhton-lighting-up-the-neopixel-rgb-led
"""
# Import necessary libraries
from machine import Pin
import neopixel
import time

# Initialize Neopixel RGB LED on pin GP18
pixels = neopixel.NeoPixel(Pin(18), 2)
# Clear Neopixel RGB LED
pixels.fill((0, 0, 0))
# Set pixel brightness
pixels.brightness = 0.5

# Define each colour codes in RGB decimal format
RED = (255, 0, 0)
ORANGE = (255,180,0)
YELLOW = (80, 80, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (100, 100, 100)

# Group all the colours in an array
colour = [RED,ORANGE,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE]

while True:
    # Light up the neopixel RGB LED and change the colour every 0.15s
    for i in range(len(colour)):
        pixels.fill(colour[i])
        pixels.write()
        time.sleep(0.5)
