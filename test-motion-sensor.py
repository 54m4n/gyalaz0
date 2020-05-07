import RPi.GPIO as GPIO
import time
import random
import os
import subprocess
import datetime



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

motion = 40 #motion pin num


GPIO.setup(motion, GPIO.IN)
state = GPIO.input(motion)

state = 0

state = GPIO.input(motion)

time.sleep(1)

while True:
    if(GPIO.input(motion)):
        most = datetime.datetime.now().strftime("%H:%M:%S")
        print("MOTION"),
	print(most)
	time.sleep(1)
    else:
        print("stop")
	time.sleep(1)

GPIO.cleanup()
