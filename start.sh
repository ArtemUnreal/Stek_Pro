#!/bin/bash

# Путь к окружению Anaconda
CONDA_ENV_NAME="iot_env"
REPO_URL="https://github.com/ArtemUnreal/Stek_Pro.git"
CLONE_DIR="$HOME/Desktop/modules/clone"

# Создание необходимых директорий, если их нет
if [ ! -d "$HOME/Desktop/modules" ]; then  
  echo "Создаем директории $HOME/Desktop/modules"
  mkdir -p "$HOME/Desktop/modules"
fi

if [ ! -d "$CLONE_DIR" ]; then
  echo "Клонируем репозиторий $REPO_URL в $CLONE_DIR"
  git clone "$REPO_URL" "$CLONE_DIR"
else
  echo "Репозиторий уже клонирован."
fi

echo "Копируем файлы и директории в $HOME/Desktop/modules"
cp -r "$CLONE_DIR"/* "$HOME/Desktop/modules/"

if ! command -v conda &> /dev/null; then
  echo "Anaconda не установлена. Устанавливаем Anaconda."
  
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh -O ~/miniconda.sh
  bash ~/miniconda.sh -b -p $HOME/miniconda
  eval "$($HOME/miniconda/bin/conda shell.bash hook)"
  
  # Добавление Anaconda в PATH
  echo "export PATH=\"$HOME/miniconda/bin:\$PATH\"" >> ~/.bashrc
  source ~/.bashrc

  rm ~/miniconda.sh
fi

# Проверка существования окружения Anaconda
if conda info --envs | grep -q "$CONDA_ENV_NAME"; then
  echo "Окружение Anaconda $CONDA_ENV_NAME найдено. Активируем его."
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate "$CONDA_ENV_NAME"
else
  echo "Окружение Anaconda $CONDA_ENV_NAME не найдено. Создаем новое."
  conda create -n "$CONDA_ENV_NAME" python=3.7 -y
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate "$CONDA_ENV_NAME"
  echo "Устанавливаем необходимые библиотеки..."
  conda install -n "$CONDA_ENV_NAME" RPi.GPIO opencv paho-mqtt -y
fi

echo "Устанавливаем Geany..."
sudo apt-get update
sudo apt-get install -y geany

echo "Запускаем Geany..."
geany &
