import RPi.GPIO as GPIO
import time
import signal
import sys
from datetime import datetime
from DBConnector import insert

GPIO.setmode(GPIO.BCM)

#Defineing Trigger and Echo pin locations on Rasp
pinTriggerLeft = 19
pinEchoLeft = 13
pinTriggerRight = 23
pinEchoRight = 24

distanceLeft = 0
distanceRight = 0

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, close)

#Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTriggerLeft, GPIO.OUT)
GPIO.setup(pinEchoLeft, GPIO.IN)
GPIO.setup(pinTriggerRight, GPIO.OUT)
GPIO.setup(pinEchoRight, GPIO.IN)

startTime1 = time.time()
stopTime1 = time.time()

startTime2 = time.time()
stopTime2 = time.time()


def SensorLeft ():
    GPIO.setup(pinTriggerLeft, GPIO.OUT)
    GPIO.setup(pinEchoLeft, GPIO.IN)
    GPIO.output(pinTriggerLeft, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerLeft, False)
    GPIO.output(pinEchoLeft, True)
    durationleft = GPIO.output(pinEchoLeft, True)


def SensorRight():
    GPIO.setup(pinTriggerRight, GPIO.OUT)
    GPIO.setup(pinEchoRight, GPIO.IN)
    GPIO.ouput(pinTriggerRight, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerRight, False)

def calculateDistanceLeft():
    SensorLeft()
    SensorLeft().durationLeft /2
    distanceLeft = SensorLeft().durationLeft /29
    print("Ping distance CM" + distanceLeft)
    time.sleep(0.5)