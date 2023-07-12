"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to display text on the OLED Display SSD1315.

CONNECTION:
Robo Pico : OLED Display
MAKER     - Oled Grove
GP2       - SDA
GP3       - SCL

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-display-text-on-oled
"""
#Import necessary libraries
import board
import busio
import adafruit_ssd1306
import time

# Define the i2c GPIOs on GP1 and GP0
#format: (board.SCL, board.SDA)
i2c = busio.I2C(board.GP3, board.GP2)

# Define the OLED display using the above pins
#format: (width, length, i2c pins)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Clear the OLED display
    oled.fill(0)
    
    # Write the data: ('text', x , y, pixel colour)
    # Pixel colour: 0 = false, 1 = true
    oled.text('Hello world!', 0, 0, 1)
    oled.text('Yeah!', 0, 25, 1)
    
    # Show the written data
    oled.show()
    time.sleep(1)
