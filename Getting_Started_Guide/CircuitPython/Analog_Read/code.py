"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read analog value on the Maker Soil.
This code applicable to other analog sensor.

CONNECTION:
Robo Pico : Maker Line
GROVE 6   - Maker Line Grove
GP27      - OUT

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-read-analog-sensor-value
Maker Soil:
https://my.cytron.io/p-maker-soil-moisture-sensor
"""
#Import necessary libraries
import board
import time
import analogio

#Define analog pin GP27 used on the board
sensor = analogio.AnalogIn(board.GP27)

while True:
    #Serial print the sensor value every 1 second
    raw_value = sensor.value
    voltage_value = (raw_value * 3.3) / 65536
    print('Raw Value : ', raw_value)
    print('Voltage Value : ', voltage_value)
    print('-------------------------')
    time.sleep(1)