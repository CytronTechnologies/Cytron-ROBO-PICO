"""
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico W to play tone
on buzzer and control NeoPixel RGB on the Robo Pico through simple webpage on localhost.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from 2023 Liz Clark for Adafruit Industries:
https://learn.adafruit.com/pico-w-http-server-with-circuitpython/code-the-pico-w-http-server
"""
import os
import time
import ipaddress
import wifi
import socketpool
import board
import microcontroller
import digitalio
import simpleio
import neopixel
from digitalio import DigitalInOut, Direction
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.methods import HTTPMethod
from adafruit_httpserver.mime_type import MIMEType


# Melody
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

# Define pin connected to piezo buzzer
PIEZO_PIN = board.GP22

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# Initialize Neopixel RGB LEDs
pixels = neopixel.NeoPixel(board.GP18, 2, brightness=0.5)
pixels.fill(0)

# Initialize buttons
btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP
    
#  connect to network
print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool, "/static")
    
def mario_tone():
    print("Play Mario Tone")
    for i in range(len(MELODY_NOTE)):
        # Play melody tones
        simpleio.tone(PIEZO_PIN, MELODY_NOTE[i], duration=MELODY_DURATION[i])
        
def rgb_red():
    print("RGB Red")
    pixels.fill(RED)  # fill the color on both RGB LEDs
    pixels.show()
    
def rgb_blue():
    print("RGB Blue")
    pixels.fill(BLUE)  # fill the color on both RGB LEDs
    pixels.show()
    
def rgb_green():
    print("RGB Green")
    pixels.fill(GREEN)  # fill the color on both RGB LEDs
    pixels.show()

def rgb_off():
    print("RGB Off")
    pixels.fill([0,0,0])  # turn off both RGB LEDs
    pixels.show()
    

#  the HTML script
def webpage():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="refresh" content="5">
    <title>Simple Webpage</title>
    </head>
    <body>
    <p>Press the button to play the tone and control RGB</p>
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="Mario Tone" value="mario_tone" type="submit">Mario Tone</button></a></p></form>
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="RGB Red" value="rgb_red" type="submit" style="color: red;">RGB Red</button></a></p></form>
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="RGB Blue" value="rgb_blue" type="submit" style="color: blue;">RGB Blue</button></a></p></form>
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="RGB Green" value="rgb_green" type="submit" style="color: green;">RGB Green</button></a></p></form>
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="RGB Off" value="rgb_off" type="submit">RGB Off</button></a></p></form>
    </body>
    </html>
    """
    return html


#  route default static IP
@server.route("/")
def base(request: HTTPRequest):  # pylint: disable=unused-argument
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

@server.route("/", method=HTTPMethod.POST)
def buttonpress(request: HTTPRequest):
    raw_text = request.raw_request.decode("utf8")
    #print(raw_text)
    if "mario_tone" in raw_text:
        mario_tone()
    if "rgb_red" in raw_text:
        rgb_red()
    if "rgb_blue" in raw_text:
        rgb_blue()
    if "rgb_green" in raw_text:
        rgb_green()
    if "rgb_off" in raw_text:
        rgb_off()
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

print("starting server..")
#  startup the server
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s" % wifi.radio.ipv4_address)
#  if the server fails to begin, restart the pico w
except OSError:
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()


while True:
    try:        
        server.poll()
    except Exception as e:
        print(e)
        continue
