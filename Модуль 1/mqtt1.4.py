import time
import paho.mqtt.client as mqtt
from rpi_ws281x import PixelStrip, Color

# Настройки для WS2812
LED_COUNT = 16        # Количество светодиодов
LED_PIN = 18          # Пин, к которому подключена лента (GPIO 18)
LED_FREQ_HZ = 800000  # Частота
LED_DMA = 10          # DMA канал
LED_BRIGHTNESS = 255  # Яркость (0-255)
LED_INVERT = False    # Инверсия сигнала
LED_CHANNEL = 0       # Канал

# Инициализация ленты
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Callback для подключения к MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Подключено с кодом {rc}")
    client.subscribe("led/command")  # Подписка на топик "led/command"

# Callback для получения сообщений из MQTT
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        print(f"Получено сообщение: {payload}")
        
        if payload.lower() == "off":
            clear_leds()  # Выключить светодиоды
        else:
            r, g, b = map(int, payload.split(','))  # Ожидаем данные в формате "255, 0, 0"
            set_color(Color(r, g, b))  # Установить указанный цвет
    except ValueError:
        print("Ошибка: некорректный формат данных")

# Функция для установки цвета светодиодов
def set_color(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

# Функция для отключения светодиодов
def clear_leds():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

# Настройка клиента MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Подключение к брокеру MQTT
client.connect("test.mosquitto.org", 1883, 60)  # Подключение к test.mosquitto.org

# Запуск клиента в отдельном потоке
client.loop_start()

try:
    while True:
        time.sleep(1)  # Основной цикл программы

except KeyboardInterrupt:
    clear_leds()  # Отключение светодиодов при завершении программы
    client.loop_stop()
    client.disconnect()




# vcc(5v) - 5v
# GND - GND
# DI - GPIO 18
