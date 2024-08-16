import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

# Создаем подкласс QMainWindow

class MyWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        # Устанавливаем размеры окна

        self.setGeometry(100, 100, 300, 200)

        # Создаем виджет QLabel и устанавливаем текст

        self.label = QLabel(self)

        self.label.setText("Привет, PyQt!")

        # Устанавливаем позицию и размеры QLabel

        self.label.setGeometry(50, 50, 200, 30)

        # Создаем кнопку QPushButton и устанавливаем текст

        self.button = QPushButton(self)

        self.button.setText("Нажми меня!")

        # Устанавливаем позицию и размеры кнопки

        self.button.setGeometry(100, 100, 100, 30)

        # Подключаем слот к сигналу нажатия кнопки

        self.button.clicked.connect(self.buttonClicked)

    # Определяем слот, который будет вызываться при нажатии кнопки

    def buttonClicked(self):

        self.label.setText("Кнопка нажата!")

# Создаем экземпляр QApplication

app = QApplication(sys.argv)

# Создаем экземпляр класса MyWindow

window = MyWindow()

# Отображаем окно

window.show()

# Запускаем главный цикл приложения

sys.exit(app.exec_())