#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse



from config import *

the_strip = None


def read_function_from_file():
    #open and read the file after the appending:
    f = open(tempfile_path, "r")
    tmp = f.read() 
    tmp = tmp.split(':')
    return tmp[0],tmp[1:]

def function_from_name(function,args=None):
    if function == 'clear':
        set_color(0,0,0)
    elif function == 'all_blue':
        set_color(0,255,0)
    elif function == 'all_red':
         set_color(255,0,0)
    elif function == 'all_green':
       set_color(0,0,255)
    elif function == 'all_pink':
        set_color(127,127,0)
    elif function == 'rainbow':
        set_rainbow_color()
    elif function == 'all_white':
        set_color(127,127,127)
    elif function == 'colorpick':
        print(args)
        set_color(int(args[0]),int(args[1]),int(args[2]))
# initializes the strip
def init():
    global the_strip
    if the_strip is None:
         # Create NeoPixel object with appropriate configuration.
        the_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        the_strip.begin()

def set_color(red,blue,green):
    colorWipe(the_strip, Color(red,blue,green), 10)

def set_rainbow_color():
    for i in range(the_strip.numPixels()):
        the_strip.setPixelColor(i, wheel(i & 255))
    the_strip.show()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    init()
    function,args = read_function_from_file()
    function_from_name(function,args)
    # Process arguments
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
#    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
#    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#    # Intialize the library (must be called once before other functions).
#    strip.begin()
#
#    print ('Press Ctrl-C to quit.')
#    if not args.clear:
#        print('Use "-c" argument to clear LEDs on exit')
#
#    try:
#
#        while True:
#            print ('Color wipe animations.')
#            colorWipe(strip, Color(255, 0, 0))  # Red wipe
#            colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#            colorWipe(strip, Color(0, 0, 255))  # Green wipe
#            print ('Theater chase animations.')
#            theaterChase(strip, Color(127, 127, 127))  # White theater chase
#            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#            print ('Rainbow animations.')
#            rainbow(strip)
#            rainbowCycle(strip)
#            theaterChaseRainbow(strip)
#
#    except KeyboardInterrupt:
#        if args.clear:
#            colorWipe(strip, Color(0,0,0), 10)
