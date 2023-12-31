"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the DC Motor on the Robo Pico DC Motor Terminals.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Tutorial link:
https://www.cytron.io/tutorial/get-started-robo-pico-circuitpython-dc-motor
"""
#Import necessary libraries
import time
import board
import pwmio
from adafruit_motor import motor

PWM_M1A = board.GP8
PWM_M1B = board.GP9
PWM_M2A = board.GP10
PWM_M2B = board.GP11

# DC motor setup
M1A = pwmio.PWMOut(PWM_M1A, frequency=10000)
M1B = pwmio.PWMOut(PWM_M1B, frequency=10000)
M2A = pwmio.PWMOut(PWM_M2A, frequency=10000)
M2B = pwmio.PWMOut(PWM_M2B, frequency=10000)
motor1 = motor.DCMotor(M1A, M1B)
motor2 = motor.DCMotor(M2A, M2B)

# Throttle value must be between -1.0 and +1.0
print("\nForwards slow")
motor1.throttle = 0.5
motor2.throttle = 0.5
time.sleep(1)

print("\nStop")
motor1.throttle = 0
motor2.throttle = 0
time.sleep(1)

print("\nForwards")
motor1.throttle = 1.0
motor2.throttle = 1.0
time.sleep(1)

print("\nStop")
motor1.throttle = 0
motor2.throttle = 0
time.sleep(1)

print("\nBackwards")
motor1.throttle = -1.0
motor2.throttle = -1.0
time.sleep(1)

print("\nStop")
motor1.throttle = 0
motor2.throttle = 0
time.sleep(1)

print("\nBackwards slow")
motor1.throttle = -0.5
motor2.throttle = -0.5
time.sleep(1)

print("\nStop")
motor1.throttle = 0
motor2.throttle = 0
time.sleep(1)