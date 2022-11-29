import time
from rpi_ws281x import Color
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip

# connect to pin 12(slot PWM)
PIN   = 12
# For Grove - WS2813 RGB LED Strip Waterproof - 30 LED/m
# there is 30 RGB LEDs.
COUNT = 30
strip = GroveWS2813RgbStrip(PIN, COUNT)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
    
    print ('Color wipe animations.')
    colorWipe(strip, Color(255, 0, 0))  # Red wipe
    colorWipe(strip, Color(0, 255, 0))  # Blue wipe
    colorWipe(strip, Color(0, 0, 255))  # Green wipe
