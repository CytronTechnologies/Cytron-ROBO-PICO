"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the DC Motor on the Robo Pico DC Motor Terminals using
MicroPython.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-dc-motor
"""
#Import necessary libraries
import time
from machine import Pin, PWM

# DC motor setup
M1A = PWM(Pin(8))
M1B = PWM(Pin(9))
M2A = PWM(Pin(10))
M2B = PWM(Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

# Throttle value must be between -1.0 and +1.0
print("\nForwards slow")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(30000)
M2A.duty_u16(0)
M2B.duty_u16(30000)
time.sleep(1)

print("\nStop")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(0)
M2B.duty_u16(0)
time.sleep(1)

print("\nForwards")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(65535)
M2A.duty_u16(0)
M2B.duty_u16(65535)
time.sleep(1)

print("\nStop")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(0)
M2B.duty_u16(0)
time.sleep(1)

print("\nBackwards")
M1A.duty_u16(65535)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(65535)
M2B.duty_u16(0)
time.sleep(1)

print("\nStop")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(0)
M2B.duty_u16(0)
time.sleep(1)

print("\nBackwards slow")
M1A.duty_u16(30000)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(30000)
M2B.duty_u16(0)
time.sleep(1)

print("\nStop")
M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
M1B.duty_u16(0)
M2A.duty_u16(0)
M2B.duty_u16(0)
time.sleep(1)