import RPi.GPIO as GPIO
import time
import threading

class Switch:
    def __init__(self, pin, changeCallback):
        self.isOn = None
        self.pin = pin
        self.changeCallback = changeCallback
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.listening = True
        self.thread = threading.Thread(None, self._listen)
        self.thread.start()
        
    def _listen(self):
        
        while self.listening:
            prev = self.isOn
            self.isOn = GPIO.input(self.pin)
            if (prev != self.isOn):
                self.changeCallback(self.isOn)
            time.sleep(.1)

