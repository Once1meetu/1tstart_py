import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

def its_clicked():
    label.setText("Он нажал на кнопышку!")

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()
button = QPushButton("Кнопышка")
label = QLabel("МетОЧКА")
layout.addWidget(button)
layout.addWidget(label)
button.clicked.connect(its_clicked)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())