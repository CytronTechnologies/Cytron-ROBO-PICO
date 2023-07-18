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
#import necessary libraries
from machine import Pin
import neopixel
import time

# Initialize the 2 Neopixel RGB LEDs on pin GP18
pixels = neopixel.NeoPixel(Pin(18), 2)
# Clear Neopixel RGB LED
pixels[0] = (0, 0, 0)
pixels[1] = (0, 0, 0)
pixels.write()
# Set pixel brightness
pixels.brightness = 0.5

while True:
    # Light up Neopixel RGB LED with purple colour
    # The sequence of the colour code is (R,G,B) input range is from 0-255 (decimal)
    pixels[0] = (200, 0, 200)
    pixels[1] = (200, 0, 200)
    pixels.write()
    time.sleep(1)
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels.write()
    time.sleep(1)
