import time
from grove.grove_rotary_angle_sensor import GroveRotaryAngleSensor

PIN = 0

sensor = GroveRotaryAngleSensor(PIN)

while True:
    print('Rotary Value: {}'.format(sensor.value))
    time.sleep(.2)
