#!/bin/bash

# Пути и настройки
VENV_PATH="/home/pi/Desktop/modules/venv"
REPO_URL="https://github.com/ArtemUnreal/Stek_Pro.git"
CLONE_DIR="/home/pi/Desktop/modules/clone"

# 1. Создаем директорию modules
mkdir -p "/home/pi/Desktop/modules"

# 2. Клонируем репозиторий (если нужно)
if [ ! -d "$CLONE_DIR" ]; then
    echo "Клонируем репозиторий..."
    git clone "$REPO_URL" "$CLONE_DIR"
else
    echo "Репозиторий уже клонирован."
fi

# 3. Копируем файлы
echo "Копируем файлы..."
cp -r "$CLONE_DIR"/* "/home/pi/Desktop/modules/"

# 4. Работа с виртуальным окружением
if [ ! -d "$VENV_PATH" ]; then
    # Создаем venv, если его нет
    echo "Создаем виртуальное окружение..."
    python3 -m venv "/home/pi/Desktop/modules/venv/bin/activate"
fi

# 5. Проверяем запись в .bashrc 
if ! grep -q "source /home/pi/Desktop/modules/venv/bin/activate" ~/.bashrc; then
    echo "Добавляем активацию в .bashrc..."
    echo "source /home/pi/Desktop/modules/venv/bin/activate" >> ~/.bashrc
fi

# 6. Устанавливаем библиотеки
echo "Устанавливаем библиотеки..."
source "/home/pi/Desktop/modules/venv/bin/activate/bin/activate"
pip install RPi.GPIO opencv-python Adafruit_DHT paho-mqtt

# 7. Устанавливаем и запускаем Geany
echo "Устанавливаем Geany..."
sudo apt-get update
sudo apt-get install -y geany

echo "Запускаем Geany..."
geany &
