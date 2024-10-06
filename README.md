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
