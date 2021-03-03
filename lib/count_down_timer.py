from threading import Thread
from time import sleep


class Countdown:
    STOPPED = "stopped"
    STARTED = "started"

    def __init__(self, seconds):
        self.seconds = float(seconds)
        self.remaining = seconds
        self.state = Countdown.STOPPED
        self.stop_flag = False
        self.on_start = None
        self.on_elapsed = None
        self.on_stop = None
        self.on_complete = None
        self.thread = Thread(target=self._start)

    def _init_thread(self):
        self.stop()
        self.thread = Thread(target=self._start)

    def stop(self):
        while self.thread.is_alive():
            self.stop_flag = True
            sleep(.1)

    def start(self):
        self._init_thread()
        self.thread.start()
        self.state = Countdown.STARTED
        if self.on_start:
            self.on_start()

    def restart(self):
        self.remaining = self.seconds
        self.start()

    def _start(self):
        prev = None
        while self.stop_flag == False and self.remaining > 0:
            sleep(.1)
            self.remaining -= .1
            seconds = int(self.remaining)
            if self.on_elapsed:
                if prev != seconds:
                    self.on_elapsed(seconds)
            prev = seconds
        self.stop_flag = False
        self.state = Countdown.STOPPED

        if self.on_stop:
            self.on_stop()
        if self.on_complete and self.remaining <= 0:
            self.on_complete()

    def is_running(self):
        return self.state == Countdown.STARTED

    def is_stopped(self):
        return self.state == Countdown.STOPPED
