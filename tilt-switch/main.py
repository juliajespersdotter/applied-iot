from machine import Pin
import time

tiltPin = Pin(27, Pin.IN)
led_pin = Pin(1, Pin.OUT)

while True:
    if tiltPin.value() == 1:
        led_pin.on()
        print("Switch ON...")
    else:
        led_pin.off()
        print("Switch OFF...")
    time.sleep_ms(500) 