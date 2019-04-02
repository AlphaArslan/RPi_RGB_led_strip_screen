#################### Import
from PIL import Image
import os
import time
import argparse
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

#################### Setup
# control panel
DEBUG = True
INFO = True
WIDTH = 32
HEIGHT = 54

# arguments handling
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to Image to be displayed")
args = vars(ap.parse_args())

# system related variables
PWD = os.path.dirname(os.path.realpath(__file__))       #returns path to project folder
IMAGE_PATH = PWD + "/" + args["image"]

# LED strip configuration GPIO.BCM
PIXEL_COUNT = WIDTH * HEIGHT
PIXEL_CLOCK = 18
PIXEL_DOUT  = 23
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()


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

    pixels.clear()

    for i in range(0 , PIXEL_COUNT):
        if (int(i/WIDTH))%2 is 0 :
            x = i%WIDTH
            y = int(i/WIDTH)
        else :
            x = WIDTH - i%WIDTH -1
            y = int(i/WIDTH)

        r ,g ,b = rgb_im.getpixel((x,y))
        pixels.set_pixel_rgb(i, r, g, b)
    # displaying image
    pixels.show()

    exit()
