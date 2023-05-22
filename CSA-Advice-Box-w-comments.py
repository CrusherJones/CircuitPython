import time, board, adafruit_hid, neopixel, random, usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard,Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
# This lets us use the QTPY2040 as a human interface device via USB
layout = KeyboardLayoutUS(kbd)
# This lets the QTPY2040 write and type on screens.
cc = ConsumerControl(usb_hid.devices)
# This is so we could control volume, or pause things, etc. Bit out of scope for this... but cool possibility

i2c = board.STEMMA_I2C()
# Creates the i2c connection we need so the gesture sensor talks to the board
apds = APDS9960(i2c)
apds.enable_gesture = True
# Lets us use gestures
apds.enable_proximity = True
# Lets us use the proximity feature of APDS9960 to read gestures

boardpixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .05)
# Creating the boardpixel means we can manipulate it
# From adafruit - "To interact with hardware in CircuitPython,
# your code must let the board know where to look for the
# hardware and what to do with it. So, you create a
# neopixel.NeoPixel() object, provide it the NeoPixel LED
# pin using the board module, and tell it the number of LEDs."
# We'll save this object to the variable "boardpixel")"

RED = (255, 0,0)
REDDISH = (145, 10, 90)
BLACK = (0, 0,0)
BLONDE = (70, 150, 50)
BLUE = (0, 0, 255)
BLUEY = (92, 59, 105)
GREEN = (0, 255, 0)
INDIGO = (75,0,130)

colors = [ RED, REDDISH, BLONDE, BLACK, BLUE, BLUEY, BLONDE, GREEN, INDIGO]
# A list of colors we can call

BS = [
"FFS. " ,
"JESUS is this a sentence or are you trying to convey the feeling of running a marathon? "
]

GOOD = [
"Drink eight glasses off water a day. " ,
"Travel with your own towel. "
]

BAD = [
"Buy that condo, sure!" ,
"Invest in pets.com"
]

ODD = [
"Look I don't even know what month it is, man." ,
"... I am a fake random machine. How would I know?"
]
# We could call this random BUT we don't want to confuse it with our random library. Try to avoid similar names!

while True:
    # Line 66 is really important - it basically means "stuff under here will run over and over
    # unless it messes up or errors out!"
    gesture = apds.gesture()
    if gesture == 0x01:
        print("You swiped 'Up' for BS")
        # why a ' there? Because we used "" for the text; can always try the reverse!
        # print(random.choice(BS)) we use the print command to print to the TERMINAL. We used "#" to grey it out here / nullify it
        layout.write(random.choice(BS))
        # Layout will write this to our machine! Make sure you test this in a separate window so you don't have BS (ha!) in your code.
        boardpixel.fill(RED)
        # This fills up the boardpixel we created with color
        time.sleep(.2)
        # This gives us a little pause before we go on
    elif gesture == 0x02:
        print("You swiped down for good advice.")
        boardpixel.fill(random.choice(colors))
        # This gives us a random color from our "colors" list
        layout.write(random.choice(GOOD))
        # Writes to screen
        time.sleep(.2)
    elif gesture == 0x03:
        print("You swiped Left for bad advice.")
        boardpixel.fill(INDIGO)
        layout.write(random.choice(BAD))
        time.sleep(.2)
    elif gesture == 0x04:
        print("You swiped Right for odd advice.")
        boardpixel.fill(GREEN)
        layout.write(random.choice(ODD))
        time.sleep(.2)
