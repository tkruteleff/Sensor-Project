from distance import *
from distanceRight import *

left = distanceLeftC
right = distanceRightC

while True:
    SensorRangeLeft()
    SensorRangeRight()

    if SensorRangeLeft(distanceLeftC) > 50:
        print ("1")