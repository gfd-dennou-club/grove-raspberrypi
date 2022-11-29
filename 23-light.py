import time
from grove.grove_light_sensor_v1_2 import GroveLightSensor

PIN = 4
sensor = GroveLightSensor(PIN)

print('Detecting light...')
while True:
    print('Light value: {0}'.format(sensor.light))
    time.sleep(1)
