import RPi.GPIO as GPIO
import time             

pir = 11            
buzzer = 13         

# Настройка GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(pir, GPIO.IN) 

try:
    while True:          
        if GPIO.input(pir) == GPIO.HIGH:
            GPIO.output(buzzer, GPIO.HIGH) 
            print("Движение обнаружено") 
        else:                
            GPIO.output(buzzer, GPIO.LOW)
            print("Нет движения") 
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
