import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.table = QTableWidget()

        self.table.setColumnCount(3)

        self.table.setRowCount(2)

        self.table.setHorizontalHeaderLabels(["Имя", "Возраст", "Город"])

        self.table.setItem(0, 0, QTableWidgetItem("Алиса"))

        self.table.setItem(0, 1, QTableWidgetItem("25"))

        self.table.setItem(0, 2, QTableWidgetItem("Лондон"))

        self.table.setItem(1, 0, QTableWidgetItem("Боб"))

        self.table.setItem(1, 1, QTableWidgetItem("30"))

        self.table.setItem(1, 2, QTableWidgetItem("Нью-Йорк"))

        self.setCentralWidget(self.table)

app = QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())