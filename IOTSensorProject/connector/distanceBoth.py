from distance import *
from distanceRight import *
import DBConnector
import Variables
import time

maxDistance = 90

while True:
    if SensorRangeRight() < maxDistance & time.time() > 5:
        if SensorRangeLeft() < maxDistance & time.time() > 5:
            Variables.visitorCount = Variables.visitorCount + 1
            print (Variables.visitorCount)
            DBConnector.insertIncrease()

    elif SensorRangeLeft() < maxDistance:
        if SensorRangeRight() < maxDistance:
            Variables.visitorCount = Variables.visitorCount - 1
            print (Variables.visitorCount)
            DBConnector.insertDelete()
