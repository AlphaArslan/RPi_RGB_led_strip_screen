##################### IMPORT #####################
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time

#################### Setup
# control panel
DEBUG = True
INFO = True
WIDTH = 32
HEIGHT = 54

# LED strip configuration
PIXEL_COUNT = WIDTH * HEIGHT
PIXEL_CLOCK = 18
PIXEL_DOUT  = 23
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()

#################### Functions
def draw_pixel(x, y, r, g, b):
    """Accessing a specific led , defined by x , y
    and assigning the (r,g,b) values to this led
    """
    # access the led
    i = get_pixel_number(x, y)
    pixels.set_pixel_rgb(i, r, g, b)

def get_pixel_number(x,y):
    """maps x y values to the sequence number of pixel
    """
    if y%2 is 0:
        i = y * WIDTH + x
    else:
        i = y * WIDTH - x
    return i

#################### Main
if __name__ == '__main__':
    # drawing pixels
    for y in range(0, HEIGHT):
        for x in range(0,WIDTH):
            draw_pixel(x, y, 255, 0, 0)

    # displaying image
    pixels.show()

    time.sleep(8)
    # drawing pixels
    for y in range(0, HEIGHT):
        for x in range(0,WIDTH):
            draw_pixel(x, y, 0, 255, 0)

    # displaying image
    pixels.show()

    time.sleep(8)

    # drawing pixels
    for y in range(0, HEIGHT):
        for x in range(0,WIDTH):
            draw_pixel(x, y, 0, 0, 255)

    # displaying image
    pixels.show()

    time.sleep(8)
