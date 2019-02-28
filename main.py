#################### Import
from PIL import Image
from rpi_ws281x import *
import os
import time

#################### Global Variables
# control panel
DEBUG = True
INFO = True
WIDTH = 30
HEIGHT = 100

# system related variables
PWD = os.path.dirname(os.path.realpath(__file__))       #returns path to project folder
IMAGE_PATH = PWD + "/var/image.jpg"

# LED strip configuration
LED_COUNT      = WIDTH*HEIGHT       # Number of LED pixels.
LED_PIN        = 18                 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000             # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5                  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255                # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False              # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0                  # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

#################### Functions
def draw_pixel(x, y, r, g, b):
    """Accessing a specific led , defined by x , y
    and assigning the (r,g,b) values to this led
    """
    # access the led
    i = get_pixel_number(x, y)
    strip.setPixelColor(i, (r,g,b))
    strip.show()

def get_pixel_number(x,y):
    """maps x y values to the sequence number of pixel
    """
    i = 5
    return i

#################### Main
if __name__ == '__main__':
    try:
        # load Image
        if DEBUG:
            print("[Debug] opening Image ..")
        im = Image.open(IMAGE_PATH)

    except IOError:
        print("[Error] Couldn't Find Image file")
        exit()

    # display the original size
    if INFO:
        print("[INFO]  original size : " + str(im.size))

    # resize Image
    if DEBUG:
        print("[Debug] Resizing Image ..")
    im = im.resize((WIDTH, HEIGHT))

    # display new size
    if INFO:
        print("[INFO]  new size : " + str(im.size))

    # access pixels
    if DEBUG:
        print("[Debug] Accessing RGB pixels ..")
    rgb_im = im.convert('RGB')

    # drawing pixels
    for x in range(0,WIDTH):
        for y in range(0, HEIGHT):
            r ,g ,b = rgb_im.getpixel((x,y))
            draw_pixel(x, y, r, g, b)
