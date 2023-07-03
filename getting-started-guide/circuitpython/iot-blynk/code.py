"""
DESCRIPTION:
This example code will uses Robo Pico and Raspberry Pi Pico W to :
1) Send value to Blnyk App
2) Read data from Blynk App
3) Control Virtual LED on Blynk App using Button 20 on Robo Pico

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from 2023 peppe80, Personal IoT App with Blynk and Raspberry PI:
https://peppe8o.com/personal-iot-with-blynk-on-raspberry-pi/
"""

import os
import ipaddress
import wifi
import socketpool
import time
import microcontroller
import board
import digitalio
import simpleio
import adafruit_requests
import ssl
import random

# Get wifi and blynk token details from a settings.toml file
ssid = os.getenv("CIRCUITPY_WIFI_SSID")
password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
blynkToken = os.getenv("blynk_auth_token")

# Buzzer
NOTE_G4 = 392
NOTE_C5 = 523
buzzer = board.GP22

# Initialize LED and button.
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

# Active LOW Push Button
pb = digitalio.DigitalInOut(board.GP20)
pb.direction = digitalio.Direction.INPUT

# Write API
def write(token,pin,value):
        api_url = "https://blynk.cloud/external/api/update?token="+token+"&"+pin+"="+value
        response = requests.get(api_url)
        if "200" in str(response):
                print("Value successfully updated")
        else:
                print("Could not find the device token or wrong pin format")
# Read API
def read(token,pin):
        api_url = "https://blynk.cloud/external/api/get?token="+token+"&"+pin
        response = requests.get(api_url)
        return response.content.decode()
    
# Connect to Wi-Fi AP
print(f"Initializing...")
wifi.radio.connect(ssid, password)
print("connected!\n")
pool = socketpool.SocketPool(wifi.radio)
print("IP Address: {}".format(wifi.radio.ipv4_address))
print("Connecting to WiFi '{}' ...\n".format(ssid), end="")
requests = adafruit_requests.Session(pool, ssl.create_default_context())

simpleio.tone(buzzer, NOTE_C5, duration=0.1)

while True:
    try:
        while not wifi.radio.ipv4_address or "0.0.0.0" in repr(wifi.radio.ipv4_address):
            print(f"Reconnecting to WiFi...")
            wifi.radio.connect(ssid, password)
            
        # Write Blynk virtual pin V0
        # V0 can be assigned to Virtual Pin Widget on Blynk App
        # Send random number
        valV0 = str(round(random.uniform(0,250),2))
        write(blynkToken,"V0",valV0)
        print(f"Write to V0: {valV0}")
        
        # Read Blynk virtual pin V1
        # V1 can be assigned to Button Widget on Blynk App
        button = read(blynkToken,"V1")
        print(f"Read V1: {button}")
        if (button == "1"):
            led.value = True
        else:
            led.value = False
        
        # Write Blynk virtual pin V2
        # V2 can be assigned to LED Widget on Blynk App
        # If the button 20 pressed it will update on the LED on Blynk App
        if (pb.value == False):
            write(blynkToken,"V2","1")
            print("LED V2: Turn ON")
        else:
            write(blynkToken,"V2","0")
            print("LED V2: Turn OFF")
        print("")
        time.sleep(2)
        simpleio.tone(buzzer, NOTE_G4, duration=0.1)
        
    except OSError as e:
        print("Failed!\n", e)
        microcontroller.reset()

