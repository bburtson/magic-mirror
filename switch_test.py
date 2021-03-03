import RPi.GPIO as GPIO
from app import App
import time
import threading


class MirrorIO:
    def __init__(self, callback):
        self.callback = callback
        self.SWITCH = 14
        self.LIGHT = 11
        self.isOpen = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LIGHT, GPIO.OUT)
        GPIO.setup(self.SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        
    def start(self):
        self.isRunning = True;
        while self.isRunning:
            self.oldIsOpen = self.isOpen

            self.isOpen = GPIO.input(self.SWITCH)
    
            self.changed = self.oldIsOpen != self.isOpen
    
            if (self.changed):
                if (self.isOpen):
                    self.callback(self.isOpen)
                    GPIO.output(self.LIGHT, GPIO.HIGH)
                else:
                    self.callback(self.isOpen)
                    GPIO.output(self.LIGHT, GPIO.LOW)        
            time.sleep(.1)

    def stop(self):
        self.isRunning = False
        GPIO.cleanup()


app = App()

def cb(result):
    if (result == 1):
        app.start()
        print('START CALLED')
    elif (result == 0):
        app.stop()
        print('STOP CALLED')

io = MirrorIO(cb)

io.start()







