from gpiozero import Servo
from lirc import RawConnection

# Пин, к которому подключен сервопривод
servo_pin = 17

# Создание объекта для управления сервоприводом
servo = Servo(servo_pin)

# Функция для обработки команд с пульта дистанционного управления
def handle_remote_command():
 	conn = RawConnection()
 	while True:
 		try:
 # Ожидание команды с пульта
 			code = conn.readline().strip()
 			print("Получена команда:", code)
 
 # Проверка кода команды и управление сервоприводом
 			if code == "BUTTON1":
 # Выполнение действий при нажатии кнопки "1"
 				servo.min()
 print("Сервопривод повернут в одну сторону")
 			elif code == "BUTTON2":
 # Выполнение действий при нажатии кнопки "2"
 				servo.mid()
 print("Сервопривод возвращен в среднее положение")
 			elif code == "BUTTON3":
 # Выполнение действий при нажатии кнопки "3"
 				servo.max()
 				print("Сервопривод повернут в другую сторону")
 
 		except KeyboardInterrupt:
 			break

try:
 	handle_remote_command()
finally:
 	servo.detach() # Отключение сервопривода при завершении программы

