from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import RPi.GPIO as GPIO
from bme280 import *
import time
import sys
import asyncio
import paho.mqtt.publish as publish

#GPIO.setwarnings(False)
MAIN_GATE=23
GARAGE_GATE=24
loop = asyncio.get_event_loop()

def bgstuff(output,delay):
   GPIO.output(output, 0)
   time.sleep(delay)
   GPIO.output(output, 1)
#   GPIO.cleanup()

def terrace(state):
   publish.single("cmnd/taras1/power", state, hostname="localhost")


def trigger_main_gate(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,bgstuff(MAIN_GATE,1))
      return HttpResponse('Main Gate has been triggered')
   else:
      return HttpResponse('Not permited.')

def trigger_garage_gate(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,bgstuff(GARAGE_GATE,0.8))
      return HttpResponse('Garage Gate has been triggered')
   else:
      return HttpResponse('Not permited.')

def turn_on_terrace_lights(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,terrace('ON'))
      return HttpResponse('Terrace lights have been turned on')
   else:
      return HttpResponse('Not permited.')

def turn_off_terrace_lights(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,terrace('OFF'))
      return HttpResponse('Terrace lights have been turned off')
   else:
      return HttpResponse('Not permited.')


def home(request):
   if request.user.is_authenticated:
      temperature,pressure,humidity = readBME280All()
      context = {
         'temperature': round(temperature,2),
         'pressure': round(pressure,2),
         'humidity': round(humidity,2),
                }
      return render(request, 'home.html', context)
   else:
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         temperature,pressure,humidity = readBME280All()
         context = {
            'temperature': round(temperature,2),
            'pressure': round(pressure,2),
            'humidity': round(humidity,2),
                   }
         return render(request, 'home.html', context)
      else:
         return render(request, 'login.html')
