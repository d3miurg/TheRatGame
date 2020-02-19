import datetime
import os
import sys
import asyncio
import pdb

class date(object):
    time = ''
        
    def __init__(self, curTime):
	    self.time = curTime

    def retTime(self):
	    return self.time

    def setTime(self, curTime):
        self.time = curTime
        

def showMainInf(message):
    try:
        print('aws')
        result = os.system('clear')
    
        if result == 1:
            os.system('cls')

        print(dat.retTime())
        print(message)

    except:
        print('show error')

async def mainLoop():

    inp = input()

    if inp == 'exit()':
        raise SystemExit

    else:
        try:
            #pdb.set_trace()
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

async def timer():
    dat.setTime(curTime = datetime.datetime.now())

async def start():
    while True:
        mainTask = asyncio.create_task(mainLoop())
        timerTask = asyncio.create_task(timer())
        
        await mainTask
        await timerTask

nowTime = datetime.datetime.now()
les = sys.stdout
dat = date(curTime = datetime.datetime.now())
showMainInf(message = '')

asyncio.run(start())
