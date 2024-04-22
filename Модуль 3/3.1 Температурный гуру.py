import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

pin = 17

while True:
	humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
	
	if humidity is not None and temp is not None:
		print("Влажность:", humidity)
		print("Температура:", temp)
	else:
		print("Ошибка")
		
	#time.sleep(2)

