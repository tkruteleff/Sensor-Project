from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    SensorRangeLeft(dleft) and SensorRangeRight(dright)

    if getattr(str(SensorRangeRight(dleft)), str(dleft)) < Variables.maxDistance:
            if getattr(str(SensorRangeLeft(dleft)), str(dleft)) < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft(dleft) < Variables.maxDistance:
        if SensorRangeRight(dright) < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
