#!/usr/bin/env python
from time import sleep
import os 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
       if ( GPIO.input(23) == False ):
              print("Printing")
              os.system("python PoemMain.py")
              print("Printed")


       sleep(1)
