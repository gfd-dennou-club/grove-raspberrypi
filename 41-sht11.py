import time
import seeed_dht

# DHT11 type
dht11 = seeed_dht.DHT("11", 26)

while True:
      humi, temp = dht11.read()
      print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(dht11.dht_type, humi, temp))
      time.sleep(1)
