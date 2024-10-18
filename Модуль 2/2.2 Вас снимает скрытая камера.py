
import RPi.GPIO as GPIO
import time
import cv2

motion_pin = 18  # Пин, к которому подключен датчик движения (GPIO 18)
buzzer_pin = 22  # Пин, к которому подключен пассивный звуковой излучатель (GPIO 22)
led_pin = 23     # Пин для светодиода (можно выбрать любой доступный GPIO)

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Инициализация камеры через OpenCV
camera = cv2.VideoCapture(0)

# Проверка, открыта ли камера
if not camera.isOpened():
    print("Ошибка: Не удалось открыть камеру")
    exit()

try:
    while True:
        if GPIO.input(motion_pin) == GPIO.HIGH:
            print("Движение обнаружено!")
            GPIO.output(led_pin, GPIO.HIGH)  # Включить светодиод
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Включить звуковой излучатель

            # Захват кадра с камеры
            ret, frame = camera.read()
            if ret:
                # Сохранение кадра на диск
                cv2.imwrite('/home/pi/motion_capture.jpg', frame)
            else:
                print("Ошибка: Не удалось захватить изображение с камеры")

            time.sleep(1)  # Задержка на 1 секунду
            
            GPIO.output(buzzer_pin, GPIO.LOW)  # Выключить звуковой излучатель
        else:
            GPIO.output(led_pin, GPIO.LOW)  # Выключить светодиод
        time.sleep(0.1)  # Добавить небольшую задержку

except KeyboardInterrupt:
    GPIO.cleanup()  # Очистка настроек GPIO при прерывании программы
    camera.release()  # Освобождение камеры
    cv2.destroyAllWindows()  # Закрытие окон OpenCV
