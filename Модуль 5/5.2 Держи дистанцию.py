import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo = 1
ik = 27

GPIO.setup(servo, GPIO.OUT)
GPIO.setup(ik, GPIO.IN)

pwm = GPIO.PWM(servo, 50)
pwm.start(0)

def control_servo(angle):
	duty = angle / 18 + 3
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	
while True:
	if GPIO.input(ik) == 0:
		control_servo(150)
		control_servo(0)

pwm.stop()
GPIO.cleanup()
