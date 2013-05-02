import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
sleeptime = 0.001
leds = []
led1 = {'num':11,'current':0.0,'freq':15,'duration':50,'state':0}
leds.append(led1)
led2 = {'num':7,'current':0.0,'freq':75,'duration':30,'state':0}
leds.append(led2)
led3 = {'num':15,'current':0.0,'freq':44,'duration':20,'state':0}
leds.append(led3)
for led in leds:
	GPIO.setup(led['num'], GPIO.OUT)
	GPIO.output(led['num'], False)
	print(led)
while True:
	for led in leds:
		led['current'] += sleeptime
		if(led['current'] >= led['freq']):
			if(led['state'] == 0):
				led['state'] = 1
				GPIO.output(led['num'], True)
				led['current'] = 0
		if(led['current'] >= led['duration']):
			if(led['state'] == 1):
				led['state'] = 0
				GPIO.output(led['num'], False)
				led['current'] = 0
for led in leds:
	GPIO.out(led['num'], False)		
