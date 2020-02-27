import os
import sys

from date import dat
from mankind import Human
from mankind import humans

def showMainInf(message):
    result = os.system('clear')
    
    if result == 1:
        os.system('cls')

    print(dat.returnTime())
    print(message)

def mainLoop():
    showMainInf(message = '')
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

les = sys.stdout
