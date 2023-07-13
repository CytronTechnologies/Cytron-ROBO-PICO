"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to light up neopixel rgb led on Robo Pico.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpyhton-lighting-up-the-neopixel-rgb-led
"""
#import necessary libraries
import board
import neopixel
import time

# Initialize the 2 Neopixel RGB LEDs on pin GP18
pixels = neopixel.NeoPixel(board.GP18, 2)
# Clear Neopixel RGB LED
pixels.fill(0)
# Set pixel brightness
pixels.brightness = 0.5

while True:
    # Light up Neopixel RGB LED with purple colour
    # The sequence of the colour code is (R,G,B) input range is from 0-255 (decimal)
    pixels.fill((200, 0, 200))
    time.sleep(1)
    pixels.fill(0)
    time.sleep(1)
