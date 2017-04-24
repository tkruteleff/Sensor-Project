from distance import *
from distanceRight import *
from DBConnector import *

while True:
    #SensorRangeLeft()
    #SensorRangeRight()

    if SensorRangeRight() > 60:
        if SensorRangeLeft() > 60:
            print ("1")
            insert1()

    if SensorRangeLeft() > 60:
        if SensorRangeRight() > 60:
            print("2")
            insert2()
