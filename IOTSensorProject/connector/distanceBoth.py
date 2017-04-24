from distance import *
from distanceRight import *

right = SensorRangeRight(distanceRightC)

while True:
    SensorRangeLeft()
    SensorRangeRight(distanceRightC)

    print("This is the distance of " + str(right))

    if distanceRightC > 50:
        print ("1")

