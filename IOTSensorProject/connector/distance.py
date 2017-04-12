import RPi.GPIO as GPIO
import time as timeNorm
import time as timeLeft
import time as timeRight
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

while True:

	GPIO.output(pinTriggerLeft, True)
	GPIO.output(pinTriggerRight, True)
	timeNorm.sleep(0.00001)
	GPIO.output(pinTriggerLeft, False)
	GPIO.output(pinTriggerRight, False)

	def SensorRangeLeft():
		GPIO.output(pinTriggerLeft,True)
		timeLeft.sleep(0.00001)
		GPIO.output(pinTriggerLeft, False)
		startTimeLeft = timeLeft.time()
		stopTimeLeft = timeLeft.time()

		while 0 == GPIO.input(pinEchoLeft):
				startTimeLeft = timeLeft.time()

		while 1 == GPIO.input(pinEchoLeft):
			stopTimeLeft = timeLeft.time()

		TimeElapsedLeft = stopTimeLeft - startTimeLeft

		distanceLeft = (TimeElapsedLeft * 34300) /2

		print ("DistanceLeft: %.1f cm" % distanceLeft)
		timeLeft.sleep(1)

	SensorRangeLeft()

	def SensorRangeRight():
		GPIO.output(pinTriggerRight, True)
		timeRight.sleep(0.00001)
		GPIO.output(pinTriggerRight, False)
		startTimeRight = timeRight.time()
		stopTimeRight = timeRight.time()


		while 0 == GPIO.input(pinEchoRight):
			startTimeRight = timeRight.time()

		while 1 == GPIO.input(pinEchoRight):
			stopTimeRight == timeRight.time()

		TimeElapsedRight = startTimeRight - stopTimeRight

		distanceRight = (TimeElapsedRight * 34300) / 2

		print("DistanceRight: %.lf cm" % distanceRight)
		timeRight.sleep(1)

	SensorRangeRight()