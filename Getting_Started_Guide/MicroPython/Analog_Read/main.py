"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read analog value on the Maker Line.
This code applicable to other analog sensor.

CONNECTION:
Robo Pico : Maker Line
GROVE 6   - Maker Line Grove
GP27      - OUT

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
"""
#Import necessary libraries
import machine
import time

#Define analog pin GP27 used on the board
sensor = machine.ADC(27)

while True:
    #Serial print the sensor value every 1 second
    raw_value = sensor.read_u16()
    voltage_value = (raw_value * 3.3) / 65536
    print('Raw Value : ', raw_value)
    print('Voltage Value : ', voltage_value)
    print('-------------------------')
    time.sleep(1)
