import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

# Создаем экземпляр приложения

app = QApplication(sys.argv)

# Создаем родительский виджет

window = QWidget()

# Создаем вертикальный макет

layout = QVBoxLayout()

# Создаем виджеты

button1 = QPushButton("Кнопка 1")

button2 = QPushButton("Кнопка 2")

label = QLabel("Метка")

# Добавляем виджеты в макет

layout.addWidget(button1)

layout.addWidget(button2)

layout.addWidget(label)

# Устанавливаем макет для родительского виджета

window.setLayout(layout)

# Отображаем окно

window.show()

# Запускаем главный цикл приложения

sys.exit(app.exec_())