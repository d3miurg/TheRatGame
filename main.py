from threading import Thread
from inp import mainLoop
from date import timer

mainThread = Thread(target = mainLoop)
timerThread = Thread(target = timer, daemon = True)

mainThread.start()
timerThread.start()
