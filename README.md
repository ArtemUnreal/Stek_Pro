Про start.sh

VENV_PATH="path/to/your/venv" - здесь нужно указывать путь к виртуальному окружению

Если файл не запускается, то прописываем это
- chmod +x start.sh
- прописывать это надо в директории с файлом, где находится start.sh


Для модуля 1.4
Чтобы заработал доступ к памяти, используем команду

sudo usermod -aG gpio <username>

В моем случае
sudo usermod -aG gpio artem

MQTT:
1) Создаём "add connection"
2) В Broker Web/Ip address пишем test.mosquitto.org
3) Создаём панель, в ней самое важное Topic, а именно тот, который указан в коде, к примеру в случае с smart_mqqt(1,4) пишем led/command

Если что, можно найти в коде, к какму топиу подключаться, а именно cleint.subscribe(" ")
