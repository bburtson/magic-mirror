# import RPi.GPIO as GPIO
from gpio_emulator.EmulatorGUI import GPIO

class Power:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def switchOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def switchOff(self):
        GPIO.output(self.pin, GPIO.LOW)
