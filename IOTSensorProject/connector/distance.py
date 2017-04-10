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
	time.sleep(0.00001)
	GPIO.output(pinTriggerLeft, False)
	GPIO.output(pinTriggerRight, False)

	def SensorRangeLeft():
		GPIO.output(pinTriggerLeft,True)
		time.sleep(0.00001)
		GPIO.output(pinTriggerLeft, False)
		startTimeLeft = time.time()
		stopTimeLeft = time.time()

		while 0 == GPIO.input(pinEchoLeft):
				startTimeLeft = time.time()

		while 1 == GPIO.input(pinEchoLeft):
			stopTimeLeft = time.time()

		TimeElapsedLeft = stopTimeLeft - startTimeLeft

		distanceLeft = (TimeElapsedLeft * 34300) /2

		print ("DistanceLeft: %.1f cm" % distanceLeft)
		time.sleep(1)


	def SensorRangeRight():
		GPIO.output(pinTriggerRight, True)
		time.sleep(0.00001)
		GPIO.output(pinTriggerRight, False)
		startTimeRight = time.time()
		stopTimeRight = time.time()


		while 0 == GPIO.input(pinEchoRight):
			startTimeRight = time.time()

		while 1 == GPIO.input(pinEchoRight):
			stopTimeRight == time.time()

		TimeElapsedRight = startTimeRight - stopTimeRight

		distanceRight = (TimeElapsedRight * 34300) / 2

		print("DistanceRight: %.lf cm" % distanceRight)