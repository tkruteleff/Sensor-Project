from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    if SensorRangeRight(dright) < Variables.maxDistance:
            if SensorRangeLeft(dleft) < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft(dleft) < Variables.maxDistance:
        if SensorRangeRight(dright) < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
