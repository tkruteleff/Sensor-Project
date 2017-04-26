from distanceRight import *
from distance import *
import Variables
import DBConnector

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
            if Variables.visitorCount <= 0:
                DBConnector.insertDelete()