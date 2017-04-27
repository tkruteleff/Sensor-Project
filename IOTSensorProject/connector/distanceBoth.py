from distanceRight import *
from distance import *
import Variables
import DBConnector

while True:

    SensorRangeLeft(), SensorRangeRight()

    while Variables.distanceRightC < Variables.maxDistance:
            if Variables.distanceLeftC < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    while Variables.distanceLeftC < Variables.maxDistance:
        if Variables.distanceRightC < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
