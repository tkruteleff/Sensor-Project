import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)

#Defineing Trigger and Echo pin locations on Rasp
pinTriggerRight = 23
pinEchoRight = 24

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, close)

#Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTriggerRight, GPIO.OUT)
GPIO.setup(pinEchoRight, GPIO.IN)

while True:

	GPIO.output(pinTriggerRight, True)
	time.sleep(0.00001)
	GPIO.output(pinTriggerRight, False)

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
		time.sleep(1)

	SensorRangeRight()
