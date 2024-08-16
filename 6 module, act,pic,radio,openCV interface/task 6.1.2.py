from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Показывает наглядно скорость роста а**2х для разных а")
        self.initUI()

    def initUI(self):
        self.label1 = QLabel("Введите 1 число")
        self.t1 = QLineEdit()
        self.label2 = QLabel("Введите 2 число")
        self.t2 = QLineEdit()

        self.t1.textChanged.connect(self.slot1)
        self.t2.textChanged.connect(self.slot2)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.t2)

        self.my_window = QWidget()
        self.my_window.setLayout(self.layout)
        self.setCentralWidget(self.my_window)

    @pyqtSlot(str)
    def slot1(self,text):
        self.label1.setText(text)

    @pyqtSlot(str)
    def slot2(self, text):
        self.label2.setText(text)

    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Up:
            a=float(self.label1.text())**2.0
            self.label1.setText(str(a))
            b=float(self.label2.text())**2.0
            self.label2.setText(str(b))
        if e.key()==Qt.Key_Down:
            a = float(self.label1.text()) ** 0.5
            self.label1.setText(str(a))
            b = float(self.label2.text()) ** 0.5
            self.label2.setText(str(b))

app = QApplication([])
window = MyApp()
window.show()
app.exec_()