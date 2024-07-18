#!/bin/bash

# Путь к виртуальному окружению
VENV_PATH="path/to/your/venv"

# Проверка, существует ли виртуальное окружение
if [ -d "$VENV_PATH" ]; then  
  echo "Виртуальное окружение найдено. Активируем его."
  source "$VENV_PATH/bin/activate"
else
  echo "Виртуальное окружение не найдено."  exit 1
fi

# Установка Geany
echo "Устанавливаем Geany..."
sudo apt-get update
sudo apt-get install -y geany

# Запуск Geany
echo "Запускаем Geany..."
geany &
