import thread
from distanceRight import *
from distance import *
import Variables
import DBConnector

thread.start_new_thread(SensorRangeLeft, ())
thread.start_new_thread(SensorRangeRight, ())


while True:
    if Variables.distanceRightC < Variables.maxDistance:
            if Variables.distanceLeftC < Variables.maxDistance:
                Variables.visitorCount = Variables.visitorCount + 1
                print (Variables.visitorCount)
                DBConnector.insertIncrease()

    elif Variables.distanceLeftC < Variables.maxDistance:
        if Variables.distanceRightC < Variables.maxDistance:
            if Variables.visitorCount > 0:
                Variables.visitorCount = Variables.visitorCount - 1
                print (Variables.visitorCount)
                DBConnector.insertDelete()
