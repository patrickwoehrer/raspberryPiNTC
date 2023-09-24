from machine
from utime

ledPin = machine.Pin(25, machine.Pin.OUT)

while True:
    ledPin.value(1)
    utime.sleep(0.5)
    ledPin.value(0)
    utime.sleep(0.5)