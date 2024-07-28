#!/bin/bash

# Путь к виртуальному окружению

VENV_PATH="$HOME/Desktop/modules/venv"

# Создание необходимых директорий, если их нет

if [ ! -d "$HOME/Desktop/modules" ]; then  
  echo "Создаем директории $HOME/Desktop/modules"
  mkdir -p "$HOME/Desktop/modules"
fi

# Проверка, существует ли виртуальное окружение
if [ -d "$VENV_PATH" ]; then  
  echo "Виртуальное окружение найдено. Активируем его."
  source "$VENV_PATH/bin/activate"
else
  echo "Виртуальное окружение не найдено. Создаем новое."  
  python3 -m venv "$VENV_PATH"
  source "$VENV_PATH/bin/activate"  
  echo "Устанавливаем необходимые библиотеки..."
  pip3 install RPi.GPIO opencv-python Adafruit_DHT
fi
  
# Установка Geany
echo "Устанавливаем Geany..."
sudo apt-get update
sudo apt-get install -y geany

# Запуск Geany с активацией виртуального окруженияecho "Запускаем Geany..."
geany &

