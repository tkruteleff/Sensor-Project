import RPi.GPIO as GPIO
import time
import Variables

GPIO.setmode(GPIO.BCM)

# Defining Trigger and Echo pin locations on Rasp
pinTriggerLeft = 19
pinEchoLeft = 13
dleft = Variables.distanceRightC

# Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTriggerLeft, GPIO.OUT)
GPIO.setup(pinEchoLeft, GPIO.IN)

# Counts the distance of the left sensor and return the value of dleft
def SensorRangeLeft(dleft):
    GPIO.output(pinTriggerLeft, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerLeft, False)
    startTimeLeft = time.time()
    stopTimeLeft = time.time()

    while 0 == GPIO.input(pinEchoLeft):
        startTimeLeft = time.time()

    while 1 == GPIO.input(pinEchoLeft):
        stopTimeLeft = time.time()

    TimeElapsedLeft = stopTimeLeft - startTimeLeft

    dleft = (TimeElapsedLeft * 34300) / 2

    if dleft < 2500:
        print ("DistanceLeft: %.1f cm" % dleft)
        time.sleep(0.5)

    return dleft
