import datetime
import time

from mankind import humans

class Date(object):
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

    def returnTime(self):
        return '{}.{}.{}: {}:{}'.format(self.day, 
                                        self.month, 
                                        self.year,
                                        self.hour,
                                        self.minute)

    def changeTime(self, step, digit):
        exec('self.{} += {}'.format(digit, step))

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

def timer():
    while True:
        time.sleep(1)
        
        dat.changeTime(step = 1, digit = 'minute')

        for i in humans:
            i.lifeCycle()

dat = Date()
