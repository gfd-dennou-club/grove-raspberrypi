import time
from grove.grove_sound_sensor import GroveSoundSensor

PIN = 2
sensor = GroveSoundSensor(PIN)

print('Detecting sound...')
while True:
    print('Sound value: {0}'.format(sensor.sound))
    time.sleep(.3)
