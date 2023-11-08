import jetFunctions as jet
import RPi.GPIO as GPIO
import time

fileName=input("Enter file name: ")

# with open(f"./{fileName}.csv",'r') as f:

one_step=5
adc_decisec=1000
data=[]
tmp_adc=[]

while True:
    try:
        steps = 0
        jet.initSpiAdc()
        jet.initStepMotorGpio()
        for i in range(0,500,one_step):
            jet.stepForward(one_step)
            time.sleep(0.005)
            for j in range(adc_decisec):
                tmp_adc.append(jet.getAdc())
                time.sleep(0.001)
            data.append([float(i),sum(tmp_adc)/len(tmp_adc)])
            tmp_adc=[]
            
        with open(f"./{fileName}.csv",'a') as f:
            for line in data:
                f.write(','.join([str(g) for g in line]))
                f.write('\n')

        print("Done")
        raise Exception
    finally:
        jet.stepBackward(500)
        time.sleep(5)
        jet.deinitStepMotorGpio()
        GPIO.cleanup()