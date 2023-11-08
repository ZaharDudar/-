import jetFunctions as jet
import RPi.GPIO as GPIO
import time

jet.initSpiAdc()
array=[]
while True:
    try:
        array.append(jet.getAdc())
        if len(array)==500:
            with open("./calibP0.csv","w") as f:
                f.write('\n'.join([str(i) for i in array]))
            break
        time.sleep(0.01)
    finally:
        GPIO.cleanup()