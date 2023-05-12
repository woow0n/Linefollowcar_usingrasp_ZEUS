
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import RPi.GPIO as GPIO
import time

class Sonic(QThread):
    mysig = Signal(int)

    def __init__(self, trig_, echo_):
        super().__init__()
        self.trig_ = trig_
        self.echo_ = echo_
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(trig_, GPIO.OUT)
        GPIO.setup(echo_, GPIO.IN)
        GPIO.output(trig_, False)

    def run(self):
        while True:
            GPIO.output(self.trig_, False)
            time.sleep(0.5)
            GPIO.output(self.trig_, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_, False)

            while GPIO.input(self.echo_) == 0:
                pulse_start = time.time()

            while GPIO.input(self.echo_) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            dist = pulse_duration * 17000
            dist = round(dist, 2)
            self.mysig.emit(dist)

    def __del__(self):
        self.quit()
