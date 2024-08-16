import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QCheckBox

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Кнопка")
        self.button.clicked.connect(self.he_clicked)
        self.label = QLabel("label")
        self.chbx = QCheckBox("Хочу кликать вечно")
        self.chbx.stateChanged.connect(self.checkboxed)
        self.count = 0

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.chbx)
        self.layout.addWidget(self.label)

        self.my_window = QWidget()
        self.my_window.setLayout(self.layout)
        self.setCentralWidget(self.my_window)

    def he_clicked(self):
        self.label.setText("Вы кликнули!")
        if not self.chbx.isChecked():
            self.button.setEnabled(False)
        self.count+=1
        print(self.count)

    def checkboxed(self):
        if self.chbx.isChecked():
            self.button.setEnabled(True)

app = QApplication(sys.argv)

window = MyApp()

window.show()

app.exec_()