import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Ввод")
        self.button.clicked.connect(self.he_clicked)
        self.label = QLabel("Введите ФИО")
        self.fio = QLineEdit()
        self.fio.textChanged.connect(self.slot)
        self.ln = QLabel("Имя")
        self.l2 = QLabel("Фамилия")
        self.lf = QLabel("Отчество")
        self.lname = QLabel("Имя")
        self.l2name = QLabel("Фамилия")
        self.lfname = QLabel("Отчество")

        self.layout = QGridLayout()
        self.layout.addWidget(self.label,1,0)
        self.layout.addWidget(self.fio,2,0)
        self.layout.addWidget(self.ln,3,0)
        self.layout.addWidget(self.l2,4,0)
        self.layout.addWidget(self.lf,5,0)
        self.layout.addWidget(self.lname,3,1)
        self.layout.addWidget(self.l2name,4,1)
        self.layout.addWidget(self.lfname,5,1)
        self.layout.addWidget(self.button,6,0)

        self.my_window = QWidget()
        self.my_window.setLayout(self.layout)
        self.setCentralWidget(self.my_window)

    @pyqtSlot(str)
    def slot(self,text):
        c=text.split(" ")
        print(c)
        if len(c) == 1:
            self.l2name.setText(c[0])
        elif len(c) == 2:
            print(len(c))
            self.lname.setText(c[1])
        elif len(c) == 3:
            self.lfname.setText(c[-1])
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка")
            self.msg.setText("Программа не поддерживает такие ФИО")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()

    def he_clicked(self):
        print("Ваши ФИО:", self.l2name.text(), self.lname.text(), self.lfname.text())


app = QApplication(sys.argv)

window = MyApp()

window.show()

app.exec_()