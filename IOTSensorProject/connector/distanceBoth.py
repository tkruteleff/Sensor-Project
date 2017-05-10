from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    SensorRangeLeft(dleft) and SensorRangeRight(dright)

    if dright < Variables.maxDistance:
            if dleft < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif dleft < Variables.maxDistance:
        if dright < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
