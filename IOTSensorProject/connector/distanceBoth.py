from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if distanceRightC > 50:
        print ("1")
