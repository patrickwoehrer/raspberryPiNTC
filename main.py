from machine import Pin, Timer
import time

boardLed = Pin(25, Pin.OUT)
blueLed = Pin(10, Pin.OUT)
redLed = Pin(11, Pin.OUT)
greenLed = Pin(12, Pin.OUT)
count = 0
i = 0
j = range(9) #only odd numbers!

def redOn():
    blueLed.value(0)
    redLed.value(1)
    greenLed.value(0)
    time.sleep(3)
    
def orangeOn():
    blueLed.value(0)
    redLed.value(1)
    greenLed.value(1)
    time.sleep(3)
    
def greenOn():
    blueLed.value(0)
    redLed.value(0)
    greenLed.value(1)
    time.sleep(3)

    
def greenBlink():
    for i in j:
        blueLed.value(0)
        redLed.value(0)
        greenLed.toggle()
        time.sleep(0.25)

while True:
    redOn()
    orangeOn()
    greenOn()
    greenBlink()
    orangeOn()