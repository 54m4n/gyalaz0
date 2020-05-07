import RPi.GPIO as GPIO
import time
import random
import os
import subprocess
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

servo = 15

GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(15,50)

stand = 6.5
rest = 2
p.start(0)


time.sleep(1)

p.ChangeDutyCycle(stand)

time.sleep(1)
p.ChangeDutyCycle(rest)
time.sleep(1)
p.ChangeDutyCycle(0)


			
p.stop()
GPIO.cleanup()

