from distance import *
from distanceRight import *
import DBConnector
import Variables
import time

maxDistance = 90

time.strftime("%H:%M")


while True:
    if SensorRangeRight() < maxDistance:
        if SensorRangeLeft() < maxDistance:
            Variables.visitorCount = Variables.visitorCount + 1
            print (Variables.visitorCount)
            DBConnector.insertIncrease()

    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            Variables.visitorCount = Variables.visitorCount - 1
            print (Variables.visitorCount)
            DBConnector.insertDelete()
