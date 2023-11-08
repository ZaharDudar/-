import jetFunctions as jet
import RPi.GPIO as GPIO
import time

jet.initSpiAdc()
array=[]
while True:
    try:
        array.append(jet.getAdc())
        print(array[-1], sum(array)/len(array))
        time.sleep(0.1)
    finally:
        GPIO.cleanup()