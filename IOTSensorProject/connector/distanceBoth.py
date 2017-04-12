import distance
import distanceRight
from threading import Thread

t1 = Thread(target = distance)
t2 = Thread(target = distanceRight)

t1.start()
t2.start()
