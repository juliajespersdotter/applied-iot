from machine import Pin
import utime as time
from dht import DHT11

pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    time.sleep(2)
    try:
        sensor.measure()
        t = sensor.temperature()
        time.sleep(2)
        h = sensor.humidity()
    except Exception as error:
        print("Exception occurred", error)
        pass 
    print("Temperature: {}".format(t))
    print("Humidity: {}".format(h))