from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QComboBox, QVBoxLayout

class Example(QWidget):#метка и комбобокс
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        line_edit=QLineEdit()
        line_edit.setText("Здесь можно писать")
        text=line_edit.text()
        print(text)

        cmb=QComboBox()
        cmb.addItem("Опция 1")
        cmb.addItem("Опция 2")
        cmb.addItem("Опция 3")
        selected=cmb.currentText()
        print(selected)

        layout=QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(cmb)

        self.setLayout(layout)
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Example')
        self.show()

app=QApplication([])
ex=Example()
app.exec_()

