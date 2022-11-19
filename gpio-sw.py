from grove.grove_switch import GroveSwitch
import time

PIN = 16
swicth = GroveSwitch(PIN)

while True:
  if swicth.state:
    print("high")
  else:
    print("low")
  time.sleep(1)
