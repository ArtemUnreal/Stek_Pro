import RPi.GPIO as GPIO
import time
import cv2

# Параметры подключенных устройств
MOTION_PIN = 18  # Пин датчика движения (GPIO 18)
BUZZER_PIN = 22  # Пин звукового излучателя (GPIO 22)
LED_PIN = 23     # Пин светодиода (GPIO 23)

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Инициализация камеры через OpenCV
camera = cv2.VideoCapture(0)

# Проверка, открыта ли камера
if not camera.isOpened():
    print("Ошибка: Не удалось открыть камеру")
    GPIO.cleanup()
    exit()

try:
    while True:
        # Проверка срабатывания датчика движения
        if GPIO.input(MOTION_PIN) == GPIO.HIGH:
            print("Движение обнаружено!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Включить светодиод
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Включить звуковой излучатель

            # Захват кадра с камеры
            ret, frame = camera.read()
            if not ret:
                print("Ошибка: Не удалось захватить изображение с камеры")
            else:
                try:
                    # Сохранение кадра на диск
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    filename = f'/home/pi/motion_capture_{timestamp}.jpg'
                    cv2.imwrite(filename, frame)
                    print(f"Кадр сохранён: {filename}")
                except Exception as e:
                    print(f"Ошибка при сохранении изображения: {e}")

            time.sleep(1)  # Задержка на 1 секунду

            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Выключить звуковой излучатель
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Выключить светодиод

        time.sleep(0.1)  # Небольшая задержка для уменьшения нагрузки на CPU

except KeyboardInterrupt:
    print("Программа прервана пользователем.")

finally:
    try:
        GPIO.cleanup()  # Очистка настроек GPIO
    except Exception as e:
        print(f"Ошибка при очистке GPIO: {e}")

    try:
        camera.release()  # Освобождение камеры
    except Exception as e:
        print(f"Ошибка при освобождении камеры: {e}")

    try:
        cv2.destroyAllWindows()  # Закрытие окон OpenCV
    except Exception as e:
        print(f"Ошибка при закрытии окон OpenCV: {e}")
