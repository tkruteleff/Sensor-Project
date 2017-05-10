import RPi.GPIO as GPIO
import time
import signal
import sys
import Variables

GPIO.setmode(GPIO.BCM)

# Defining Trigger and Echo pin locations on Rasp
pinTriggerRight = 23
pinEchoRight = 24
dleft = Variables.distanceRightC


def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)

# Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTriggerRight, GPIO.OUT)
GPIO.setup(pinEchoRight, GPIO.IN)


def SensorRangeRight(dleft):
    GPIO.output(pinTriggerRight, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerRight, False)

    GPIO.output(pinTriggerRight, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerRight, False)
    startTime = time.time()
    stopTime = time.time()

    while 0 == GPIO.input(pinEchoRight):
        startTime = time.time()

    while 1 == GPIO.input(pinEchoRight):
        stopTime = time.time()

    TimeElapsed = stopTime - startTime

    dleft = (TimeElapsed * 34300) / 2

    print ("DistanceRight: %.1f cm" % dleft)
    time.sleep(1)

    return dleft
