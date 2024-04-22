from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led = 11
button = 13

GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(button) == GPIO.HIGH:
		GPIO.output(led,GPIO.HIGH)
		print("Свет есть")
	else:
		GPIO.output(led,GPIO.LOW)
		print("Света нет")
	sleep(0.1)
	
GPIO.cleanup()
