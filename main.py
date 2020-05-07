import RPi.GPIO as GPIO
import time
import random
import os
import subprocess
import datetime
#importing fucking libraries

GPIO.setwarnings(False)		#this is because we do not want to alerted by any fucking nonsense error
GPIO.setmode(GPIO.BOARD)	#ass gpio can be board/bcm, here u are -> google: board vs bcm

motion = 40		#motion sensor fucking pin number
servo = 15		#servo sensor shit pin num

GPIO.setup(motion, GPIO.IN)		#pir sensor is an input
GPIO.setup(servo, GPIO.OUT)		#servo sensor is an output

p = GPIO.PWM(15,50)		#setting up the servo. we need to repeat the impulses, and we know period time is the reciprocal of the frequency, so 15/50 will be good... I don't know what I am talking about...

stand = 6.5		#I do not know nothing about volts or ampers. I do not give a shit, but this is what we calculated to 90 degree
rest = 2		#2 equals 0 degree, so this is the position when the figure is "sleeping"
p.start(0)		#I have no idea why, but 2 or 0 is equal, but we need to start from here to avoid the "tremor" of the servo

time.sleep(3)
while True:		#doing all of this shit while we stop the program
	if(GPIO.input(motion)):			#if motion detected
		time.sleep(0.1) 			#wait before servo
		p.ChangeDutyCycle(stand)	#stand up
		os.system("python /home/pi/Desktop/gyalazo-v5/gyalazo.py 1")	#call the program exactly
	
		time.sleep(1)				#dramatic pause after the abusing
		p.ChangeDutyCycle(rest)		#go back to sleep
		time.sleep(0.1)				#wait 100ms
		p.ChangeDutyCycle(0)		#some kind of 'stopping' the servo thing... no position changes, but tremor stops
		rsleep=random.randrange(10, 40, 1)		#10-40 seconds we want to sleep, that is more natural behavior	
		most = datetime.datetime.now().strftime("%Y. %m. %d. %H:%M:%S")		#get the actual date and time for the log
		
		fin = open("/home/pi/Desktop/gyalazo-v5/res/result.txt", "r")		#result.txt contains the last generated fucking abusion sentence
		data2 = fin.read()		#read that shit to data2
		fin.close()		#close that fuck file
		fout = open("/home/pi/Desktop/gyalazo-v5/log/log.txt", "a")		#open log.txt shit
		fout.write(str(most) + " | " + "rest: " + str(rsleep) + " | " + str(data2) + '\n')		#paste interesting information for the future: actual time | generated resting time | sentence of glory
		fout.close()		#close that fuck too
		time.sleep(rsleep)	#random pause before next rage
		
	else:
		time.sleep(1)		#if nothing happens, wait 1 more second
			
p.stop()		#stop all of this shit, you will never get here..
GPIO.cleanup()	#clean all the gpio settings

