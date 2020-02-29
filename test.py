import time

from date import dat
from mankind import humans
from mankind import Human
from datetime import datetime

asd = Human()
n = 0

def tst():
    n = 0

    time.sleep(0.995150)
        
    dat.changeTime(step = 1, digit = 'minute')

    if n != 510100000:
        #asd = Human()
        n += 1

    for i in humans:
        i.lifeCycle()

def ssao():
    print(datetime.now())
    
    while True:
        asd.lifeCycle()
        print(datetime.now())

