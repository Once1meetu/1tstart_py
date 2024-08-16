import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Кнопка")
        self.button.clicked.connect(self.he_clicked)
        self.label = QLabel("label")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.my_window = QWidget()
        self.my_window.setLayout(self.layout)
        self.setCentralWidget(self.my_window)

    def he_clicked(self):
        self.label.setText("Вы кликнули!")
        self.button.setEnabled(False)

app = QApplication(sys.argv)

window = MyApp()

window.show()

app.exec_()