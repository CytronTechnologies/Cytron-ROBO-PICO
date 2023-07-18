"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to display text on the OLED Display SSD1315 using MicroPython.

CONNECTION:
Robo Pico : OLED Display
Grove 1   - Oled Grove
GP0       - SDA
GP1       - SCL

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-display-text-on-oled
"""
#Import necessary libraries
from machine import Pin, SoftI2C
import ssd1306
import framebuf
import time

# Define the i2c GPIOs on GP1 and GP0
#format: (board.SCL, board.SDA)
i2c = SoftI2C(scl=Pin(1), sda=Pin(0))   


# Define the OLED display using the above pins
#format: (width, length, i2c pins)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    #Clear the OLED display
    oled.fill(0)
    
    #Write the data: ('text', x , y, pixel colour)
    #Pixel colour: 0 = false, 1 = true
    oled.text('Hello world!', 0, 0, 1)
    oled.text('Yeah!', 0, 25, 1)
    
    #Show the written data
    oled.show()
    time.sleep(1)
