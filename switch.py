#!/usr/bin/python3
import requests
import json
import datetime
import time
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
GPIO.setmode(GPIO.BCM)
from homemgmt import terrace

while True:

   current_time = datetime.datetime.now().timestamp()
   print("Current Time =", current_time)

   r=requests.get('https://api.sunrise-sunset.org/json?lat=51.9720207&lng=21.0345007&formatted=0')
   dict=json.loads(r.text)
   sunrise=str(dict['results']['sunrise']).replace('+00:00', 'Z')
   sunrise=datetime.datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%SZ").timestamp()

   sunset=str(dict['results']['sunset']).replace('+00:00', 'Z')
   sunset=datetime.datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%SZ").timestamp()

   #print("Sunrise: "+str(sunrise))
   print("Sunset:  "+str(sunset))
   if current_time >= sunset:
      terrace(1)
      print(1)
   else:
      terrace(0)
      print(0)
   time.sleep(3600)

