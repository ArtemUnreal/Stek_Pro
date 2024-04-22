from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led = 11
GPIO.setup(led,GPIO.OUT)
while True:
	GPIO.output(led,GPIO.HIGH)
	sleep(1)
	GPIO.output(led,GPIO.LOW)
	sleep(1)
	
GPIO.cleanup()
