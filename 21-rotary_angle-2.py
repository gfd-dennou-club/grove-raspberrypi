import time
from grove.adc import ADC

adc = ADC()
while True:
    # Read channel 0(Slot A0) voltage. Max 3300 mV
    print( int( adc.read_voltage(0) / 3300 * 100 ) )  # val 0-1000
    time.sleep(1)
