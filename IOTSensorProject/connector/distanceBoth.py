from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if SensorRangeRight() < 60:
        if SensorRangeLeft() < 60:
            print ("1")

    if SensorRangeLeft() < 60:
        if SensorRangeRight() < 60:
            print("2")