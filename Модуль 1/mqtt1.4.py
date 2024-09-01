import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def set_color(r, g, b):
	GPIO.output(RED_PIN, GPIO.HIGH if r else GPIO.LOW)
	GPIO.output(GREEN_PIN, GPIO.HIGH if g else GPIO.LOW)
	GPIO.output(BLUE_PIN, GPIO.HIGH if b else GPIO.LOW)

def on_message(client, userdata, message):
	msg = message.payload.decode("utf-8")
	print(f"Received message: {msg}")
	
	try:
		r, g, b = map(int, msg.split(','))
		set_color(r, g, b)
	except ValueError:
		print("Invalid message format. Expected 'R, G, B'. ")
	
client = mqtt.Client()
client.on_message = on_message

broker_address = "test.mosquitto.org"
client.connect(broker_address, port=1883)

client.subscribe("home/rgb_led")
client.loop_forever()
