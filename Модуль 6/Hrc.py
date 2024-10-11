import RPi.GPIO as GPIO
import time

# Определение пинов
TRIG = 23
ECHO = 24

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Отправка ультразвукового сигнала
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Засекаем время отклика
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Вычисление расстояния
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # 34300 см/с - скорость звука

    return distance

try:
    while True:
        dist = distance()
        print(f"Расстояние: {dist:.2f} см")
        time.sleep(1)
except KeyboardInterrupt:
    print("Измерение прервано пользователем")
    GPIO.cleanup()
