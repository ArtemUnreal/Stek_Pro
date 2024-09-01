#!/bin/bash

# Путь к виртуальному окружению
VENV_PATH="$HOME/Desktop/modules/venv"
REPO_URL="https://github.com/ArtemUnreal/Stek_Pro.git"
CLONE_DIR="$HOME/Desktop/modules/clone"

# Создание необходимых директорий, если их нет
if [ ! -d "$HOME/Desktop/modules" ]; then  
  echo "Создаем директории $HOME/Desktop/modules"
  mkdir -p "$HOME/Desktop/modules"
fi

# Клонирование репозитория
if [ ! -d "$CLONE_DIR" ]; then
  echo "Клонируем репозиторий $REPO_URL в $CLONE_DIR"
  git clone "$REPO_URL" "$CLONE_DIR"
else
  echo "Репозиторий уже клонирован."
fi

# Копирование файлов и директорий в /Desktop/modules
echo "Копируем файлы и директории в $HOME/Desktop/modules"
cp -r "$CLONE_DIR"/* "$HOME/Desktop/modules/"

# Проверка, существует ли виртуальное окружение
if [ -d "$VENV_PATH" ]; then  
  echo "Виртуальное окружение найдено. Активируем его."
  source "$VENV_PATH/bin/activate"
else
  echo "Виртуальное окружение не найдено. Создаем новое."  
  python3 -m venv "$VENV_PATH"
  source "$VENV_PATH/bin/activate"  
  echo "Устанавливаем необходимые библиотеки..."
  pip3 install RPi.GPIO opencv-python Adafruit_DHT paho-mqtt
fi
  
# Установка Geany
echo "Устанавливаем Geany..."
sudo apt-get update
sudo apt-get install -y geany

# Запуск Geany с активацией виртуального окружения
echo "Запускаем Geany..."
geany &