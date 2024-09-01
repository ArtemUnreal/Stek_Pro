import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = False

def on_message(client, userdata, message):
	global led_state
	msg = message.payload.decode("utf-8")
	print(f"Received message: {msg}")
	
	led_state = not led_state
	GPIO.output(LED_PIN, GPIO.HIGH if led_state else GPIO.LOW)
	
client = mqtt.Client()
client.on_message = on_message

broker_address = "test.mosquitto.org"
client.connect(broker_address, port=1883)

client.subscribe("home/led")
client.loop_forever()
