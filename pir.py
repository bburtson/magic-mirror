
from lib.power import Power
from lib.switch import Switch
from app import App
from lib.obj import Obj
import time

# import RPi.GPIO as GPIO
from gpio_emulator.EmulatorGUI import GPIO


settings = Obj()
settings.lastMotionEndTime = None
settings.maxIdleSeconds = 10


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

light = Power(4)
app = App()
Power(14).switchOn()


def is_idle(): return settings.lastMotionEndTime != None
def calcSecondsIdle(): return int(time.time() - settings.lastMotionEndTime)
def resetIdleCountdown(): settings.lastMotionEndTime = None


def onMotionSwitchChange(value):
    if (value):
        light.switchOn()
        resetIdleCountdown()
        if(app.is_running == False):
            app.start()
            print("Started")
    else:
        light.switchOff()
        settings.lastMotionEndTime = time.time()


Switch(15, onMotionSwitchChange)

while True:
    if (is_idle()):
        idle = calcSecondsIdle()
        print(idle)
        if(idle >= settings.maxIdleSeconds):
            resetIdleCountdown()
            app.stop()
            print("Stopped")
    time.sleep(1)


GPIO.cleanup()
