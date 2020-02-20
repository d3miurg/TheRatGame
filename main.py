import datetime
import os
import sys
import asyncio
import pdb
import time

class date(object):
    minute = 0
    hour = 0
    day = 0
    mounth = 0
    year = 0
        
    def __init__(self):
        dt = datetime.datetime.now()
        self.minute = dt.minute
        self.hour = dt.hour
        self.day = dt.day
        self.month = dt.month
        self.year = dt.year

    def retTime(self):
        return '{}.{}.{}: {}:{}'.format(self.day,
                                           self.month,
                                           self.year,
                                           self.hour,
                                           self.minute)

    def changeTime(self):
        self.minute += 1

        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        if self.hour == 24:
            self.day += 1
            self.hour = 0
        
        if self.day == 28:
            if self.month == 2 and self.year % 4 != 0:
                self.month += 1
                self.day = 1

        if self.day == 29:
            if self.month == 2 and self.year % 4 == 0:
                self.month += 1
                self.day = 1

        if self.day == 31:
            if self.month % 2 == 0 and self.month <= 7:
                self.month += 1
                self.day = 1

            elif self.month % 2 != 0 and self.month >= 7:
                self.month += 1
                self.day = 1

        if self.day == 32:
            if self.month % 2 != 0 and self.month <= 7:
                self.month += 1
                self.day = 1

            elif self.month % 2 == 0 and self.month >= 7:
                self.month += 1
                self.day = 1

        if self.month == 13:
            year += 1
            month = 1

def showMainInf(message):
    result = os.system('clear')
    
    if result == 1:
        os.system('cls')

    print(dat.retTime())
    print(message)

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
    time.sleep(1)
    dat.changeTime()                            

async def start():
    while True:
        mainTask = asyncio.create_task(mainLoop())
        timerTask = asyncio.create_task(timer())
        
        await mainTask
        await timerTask

nowTime = datetime.datetime.now()
les = sys.stdout
dat = date()

showMainInf(message = '')

asyncio.run(start())
