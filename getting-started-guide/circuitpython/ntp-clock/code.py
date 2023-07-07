"""
DESCRIPTION:
This example code will demonstrate how to grab time from the internet
through Network Time Protocol (NTP).
This demo code is written in CircuitPython.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from 2022 Carter Nelson for Adafruit Industries:
https://learn.adafruit.com/super-simple-sunrise-lamp/code

MORE INFO:
https://cytron.io/p-robo-pico-simplifying-robotics-with-raspberry-pi-pico
https://circuitpython.org/board/raspberry_pi_pico_w
"""

import os
import time
import rtc
import socketpool
import wifi
import adafruit_ntp

# Time zone offset in hours from UTC
# Malaysia/Singapore GMT = +8
# Thailand GMT = +7
# Vietnam GMT = +7
# Germany GMT = +2
# United Kingdom GMT = +1
# Find your country GMT through this link:
# https://greenwichmeantime.com/time-zone/world/

TZ_OFFSET = +8  

# Connect to local network
# Retrive your Wifi SSID and password from settings.toml file
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
print("Wifi connected.")

# Get current time using NTP
print("Fetching time from NTP.")
pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=TZ_OFFSET, socket_timeout=20)
rtc.RTC().datetime = ntp.datetime


while True:
    now = time.localtime()
    # Print current time in format hh:mm:ss
    print("Current time: {:2}:{:02}:{:02}".format(now.tm_hour, now.tm_min, now.tm_sec))
    time.sleep(1)

