import time, board, adafruit_hid, neopixel, random, usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard,Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
cc = ConsumerControl(usb_hid.devices)
# This is so we could control volume, or pause things, etc. Bit out of scope for this... but cool possibility

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_gesture = True
apds.enable_proximity = True

boardpixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .05)

RED = (255, 0,0)
REDDISH = (145, 10, 90)
BLACK = (0, 0,0)
BLONDE = (70, 150, 50)
BLUE = (0, 0, 255)
BLUEY = (92, 59, 105)
GREEN = (0, 255, 0)
INDIGO = (75,0,130)

colors = [ RED, REDDISH, BLONDE, BLACK, BLUE, BLUEY, BLONDE, GREEN, INDIGO]

BS = [
"FFS. " ,
"... delete that. "
]

GOOD = [
"Drink eight glasses off water a day. " ,
"Travel with your own towel. "
]

BAD = [
"Buy that condo, sure! " ,
"Invest in pets.com "
]

ODD = [
"Look I don't even know what month it is, man. " ,
"... I am a fake random machine. How would I know? "
]

while True:
    gesture = apds.gesture()
    if gesture == 0x01:
        print("You swiped 'Up' for BS")
        layout.write(random.choice(BS))
        boardpixel.fill(RED)
        time.sleep(.2)
    elif gesture == 0x02:
        print("You swiped down for good advice.")
        boardpixel.fill(random.choice(colors))
        layout.write(random.choice(GOOD))
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
