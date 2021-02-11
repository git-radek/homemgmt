import RPi.GPIO as GPIO
from bme280 import *
import time
import sys
import paho.mqtt.publish as publish


GPIO.setwarnings(False)
MAIN_GATE = 23
GARAGE_GATE = 24
OUTTER_LIGHTS = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(MAIN_GATE, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GARAGE_GATE, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(OUTTER_LIGHTS, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.output(MAIN_GATE, 0)

def terrace(state):
   publish.single("cmnd/taras1/power", state, hostname="localhost", keepalive=60)
   if state == 1:
      GPIO.output(OUTTER_LIGHTS, 0)
   else:
      GPIO.output(OUTTER_LIGHTS, 1)

