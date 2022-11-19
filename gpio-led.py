import time
from grove.grove_led import GroveLed

PIN   = 5
led = GroveLed(PIN)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
