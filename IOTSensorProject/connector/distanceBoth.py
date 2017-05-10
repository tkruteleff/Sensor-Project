from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    if SensorRangeRight(Variables).distanceRightC < Variables.maxDistance:
            if SensorRangeLeft(Variables).distanceLeftC < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif SensorRangeLeft(Variables).distanceLeftC < Variables.maxDistance:
        if SensorRangeRight(Variables).distanceRightC < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
