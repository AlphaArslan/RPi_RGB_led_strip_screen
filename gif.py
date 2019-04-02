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
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()

#################### Functions
def get_row_num(i):
    return int(i/WIDTH)


#################### Main
if __name__ == '__main__':
    pixels.clear()
    pixels.show()

    while True:
        for line in range(0, HEIGHT-2)
            # drawing pixels
            for i in range(0, PIXEL_COUNT):
                if get_row_num(i) is line :
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 255, 255, 255))
                else:
                    pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 0, 255, 0))

            # displaying image
            pixels.show()
            time.sleep(0.5)
