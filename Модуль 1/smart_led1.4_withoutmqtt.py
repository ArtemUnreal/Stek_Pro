import time
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

try:
    while True:
        command = input("Введите цвет в формате 'r, g, b' или 'off' для выключения: ")
        if command.lower() == "off":
            clear_leds()
        else:
            try:
                r, g, b = map(int, command.split(','))
                set_color(Color(r, g, b))
            except ValueError:
                print("Ошибка: некорректный формат данных. Попробуйте снова.")
except KeyboardInterrupt:
    clear_leds()
    print("\nПрограмма завершена.")
