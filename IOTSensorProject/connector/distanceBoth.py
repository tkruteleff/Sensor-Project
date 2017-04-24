from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    print("This is the distance of " + str(SensorRangeRight()))
    print("This is the distance of " + str(SensorRangeLeft()))
    if SensorRangeRight() < 60:
        if SensorRangeLeft() < 60:
            print ("1")