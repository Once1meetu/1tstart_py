from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QRadioButton, QComboBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        line_edit=QLineEdit(self)
        line_edit.setGeometry(10,10,200,25)
        line_edit.setText("Введите текст: ")
        text=line_edit.text()
        print(text)

        radio_btn=QRadioButton(self)
        radio_btn.setGeometry(10,50,200,25)
        radio_btn.setText("Выберите ответ:")
        state=radio_btn.isChecked()
        print(state)

        cmb=QComboBox(self)
        cmb.setGeometry(10,90,200,25)
        cmb.addItem("Опция 1")
        cmb.addItem("Опция 2")
        selected=cmb.currentText()
        print(selected)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Example')
        self.show()

app=QApplication([])
ex=Example()
app.exec_()
#В продолжении работа с БД учёток
