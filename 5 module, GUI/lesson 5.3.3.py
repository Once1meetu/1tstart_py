import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

# Создаем экземпляр приложения

app = QApplication(sys.argv)

# Создаем родительский виджет

window = QWidget()

# Создаем вертикальный макет

layout = QVBoxLayout()

# Создаем метку

label = QLabel("Введите ваше имя:")

layout.addWidget(label)

# Создаем текстовое поле

text_field = QLineEdit()

layout.addWidget(text_field)

# Создаем кнопку

button = QPushButton("Привет!")

layout.addWidget(button)

# Функция-обработчик для кнопки

def say_hello():

    name = text_field.text()

    message = f"Привет, {name}!"

    QMessageBox.information(window, "Приветствие", message)

# Подключаем функцию-обработчик к сигналу clicked кнопки

button.clicked.connect(say_hello)

# Устанавливаем макет для родительского виджета

window.setLayout(layout)

# Отображаем окно

window.show()

# Запускаем главный цикл приложения

sys.exit(app.exec_())