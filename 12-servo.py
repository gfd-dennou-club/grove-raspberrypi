from grove.grove_servo import GroveServo
import time

pin = 12
servo = GroveServo(pin)

while True:
    for x in range(0, 180):
        print(x, "degree")
        servo.setAngle(x)
        time.sleep(0.05)
    for x in range(180, 0, -1):
        print(x, "degree")
        servo.setAngle(x)
        time.sleep(0.05)
