from distance import *
from distanceRight import *

while True:
    SensorRangeLeft()
    SensorRangeRight()

    if SensorRangeLeft().distanceLeftC <= 50:
        print("1")