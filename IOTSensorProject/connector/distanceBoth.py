from distanceRight import *
from distance import *
import Variables
import DBConnector


while True:
    while SensorRangeRight() < Variables.maxDistance:
        # if SensorRangeLeft() < Variables.maxDistance:
        Variables.visitorCount = Variables.visitorCount + 1
        print (Variables.visitorCount)
    DBConnector.insertIncrease()

    while SensorRangeLeft() < Variables.maxDistance:
        # if SensorRangeRight() < Variables.maxDistance:
        Variables.visitorCount = Variables.visitorCount - 1
        print (Variables.visitorCount)
    if Variables.visitorCount <= 0:
        DBConnector.insertDelete()
