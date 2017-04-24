from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight(distanceRightC)

    if distanceRightC > 50:
        print ("1")
