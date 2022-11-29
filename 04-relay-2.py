import time
from grove.grove_relay import GroveRelay

PIN   = 18
relay = GroveRelay(PIN)

while True:
    relay.on()
    time.sleep(1)
    relay.off()
    time.sleep(1)
