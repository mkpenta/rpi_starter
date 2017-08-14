import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
	input = GPIO.input(18)
	if input == True:
		print('Button Pressed')
		time.sleep(0.2)	
	
