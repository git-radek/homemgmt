import RPi.GPIO as GPIO
from bme280 import *
import time
import sys
GPIO.setwarnings(False)
MAIN_GATE = 23
GARAGE_GATE = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(MAIN_GATE, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GARAGE_GATE, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.output(MAIN_GATE, 0)
