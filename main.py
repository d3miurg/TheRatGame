import os
import sys
import time

from date import dat
from threading import Thread

def showMainInf(message):
    result = os.system('clear')
    
    if result == 1:
        os.system('cls')

    print(dat.returnTime())
    print(message)

def mainLoop():
    while True:
        inp = input()

        if inp == 'exit()':
            raise SystemExit

        else:
            try:
                sys.stdout = open('temp.txt', 'w')
            
                exec(inp)
            
                sys.stdout.close()
                sys.stdout = les

                curOut = open('temp.txt', 'r')
                showMainInf(message = curOut.read())
                curOut.close()

            except Exception as e:
                sys.stdout.close()
                sys.stdout = les
                showMainInf(message = e)

def timer():
    while True:
        time.sleep(1)
        dat.changeTime()

        if mainThread.is_alive() == False:
            break

les = sys.stdout

showMainInf(message = '')

mainThread = Thread(target = mainLoop)
timerThread = Thread(target = timer)

mainThread.start()
timerThread.start()
