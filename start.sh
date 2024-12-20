#!/bin/bash

# Путь к виртуальному окружению
VENV_PATH="/home/pi/Desktop/modules/venv"
REPO_URL="https://github.com/ArtemUnreal/Stek_Pro.git"
CLONE_DIR="/home/pi/Desktop/modules/clone"

# Создаем директорию modules, если она еще не создана
if [ ! -d "/home/pi/Desktop/modules" ]; then
  mkdir -p "/home/pi/Desktop/modules"
fi

# Клонирование репозитория
if [ ! -d "$CLONE_DIR" ]; then
  echo "Клонируем репозиторий $REPO_URL в $CLONE_DIR"
  git clone "$REPO_URL" "$CLONE_DIR"
else
  echo "Репозиторий уже клонирован."
fi

# Копирование файлов и директорий в /Desktop/modules
echo "Копируем файлы и директории в /home/pi/Desktop/modules"
cp -r "$CLONE_DIR"/* "/home/pi/Desktop/modules/"

# Проверяем, существует ли виртуальное окружение
if [ -d "$VENV_PATH" ]; then
  # Добавляем команду активации виртуального окружения в /etc/profile
  echo 'source /home/pi/Desktop/modules/venv/bin/activate' >> /etc/profile
  echo "Команда активации виртуального окружения добавлена в /etc/profile."
else
  echo "Виртуальное окружение не найдено."
fi

echo "Запускаем Geany..."
geany &
