from grove.gpio import GPIO
import time 

pin = 16
switch = GPIO(pin, GPIO.IN)

while True:
    print (switch.read())
    time.sleep(1)


