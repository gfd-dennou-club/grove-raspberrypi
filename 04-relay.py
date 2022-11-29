from grove.gpio import GPIO
from time import sleep

pin = 22
led = GPIO(pin, GPIO.OUT)

while True:
    led.write(1)
    sleep(1)
    led.write(0)
    sleep(1)
