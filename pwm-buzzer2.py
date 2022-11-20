import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 400)  # gpio18 frequency=400Hz
p.start(0)
p.ChangeDutyCycle(2) # 2 = 0.5ms 12 = 2.4ms

time.sleep(3)

p.stop()
GPIO.cleanup()
