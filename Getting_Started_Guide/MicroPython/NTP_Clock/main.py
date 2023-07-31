
"""
DESCRIPTION:
This example code will demonstrate how to grab time from the internet
through Network Time Protocol (NTP).This demo code is written in MicroPython.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from EngineerGarage:
https://www.engineersgarage.com/micropython-esp8266-esp32-rtc-utc-local-time/
"""
from machine import RTC
import network
import ntptime
import time

# Time zone offset in hours from UTC
# Malaysia/Singapore GMT = +8
# Thailand GMT = +7
# Vietnam GMT = +7
# Germany GMT = +2
# United Kingdom GMT = +1
# Find your country GMT through this link:
# https://greenwichmeantime.com/time-zone/world/

TZ_OFFSET = +8 

WIFI_SSID = "Your-Wifi"
WIFI_PASSWORD = "Your-Password" 

# Connect to local network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(WIFI_SSID, WIFI_PASSWORD)
print("Wifi connected.")

# Get current time using NTP
print("Fetching time from NTP.")
rtc = RTC()
sec = ntptime.time() + TZ_OFFSET * 3600
(year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(sec)
rtc.datetime((year, month, day, 0, hours, minutes, seconds, 0))

while True:
    (year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime()
    print("Current time: {:2}:{:02}:{:02}".format(hours, minutes, seconds))
    time.sleep(1)
