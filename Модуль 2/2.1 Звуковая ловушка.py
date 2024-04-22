from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir = 17
buzzer = 27

GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(pir ,GPIO.IN)

while True:
	if GPIO.input(pir) == GPIO.HIGH:
		GPIO.output(buzzer,GPIO.HIGH)
		print("Движение обнаружено")
		sleep(0.01)
	else:
		GPIO.output(buzzer,GPIO.LOW)
		print("Нет движение")
	
	
GPIO.cleanup()

