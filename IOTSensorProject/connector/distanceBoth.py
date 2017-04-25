from distance import *
from distanceRight import *
import DBConnector
import Variables

maxDistance = 90

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
