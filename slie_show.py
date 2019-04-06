#################### Import
from PIL import Image
import os
import time
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

#################### Setup
# control panel
DEBUG = True
INFO = True
WIDTH = 32
HEIGHT = 54

# system related variables
PWD = os.path.dirname(os.path.realpath(__file__))       #returns path to project folder
IMAGE_PATH = PWD + "/show/"

# LED strip configuration GPIO.BCM
PIXEL_COUNT = WIDTH * HEIGHT
PIXEL_CLOCK = 11            # SPI0 SCLK
PIXEL_DOUT  = 10            # SPI0 MOSI
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()
pixels.show()

#################### Main
if __name__ == '__main__':
    while True:
        for i in range(1,9):
            try:
                # load Image
                if DEBUG:
                    print("[Debug] opening Image ..")
                im = Image.open(IMAGE_PATH + str(i) + ".jpg")

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
            pixels.show()

            time.sleep(4)
            for i in range(0 , PIXEL_COUNT):
                if (int(i/WIDTH))%2 is 0 :
                    x = i%WIDTH
                    y = int(i/WIDTH)
                else :
                    x = WIDTH - i%WIDTH -1
                    y = int(i/WIDTH)

                r ,g ,b = rgb_im.getpixel((x,y))
                pixels.set_pixel(i,  Adafruit_WS2801.RGB_to_color(b, r, g))
            # displaying image
            pixels.show()
            time.sleep(5)
            pixels.clear()
            pixels.show()
