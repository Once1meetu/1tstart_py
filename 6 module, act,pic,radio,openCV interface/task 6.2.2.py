from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication([])
widget = QWidget()
image = QLabel(widget)
pixmap = QPixmap('image.jpg')
image.setPixmap(pixmap)
image.setGeometry(0,0,pixmap.width(),pixmap.height())
widget.setGeometry(100,100,1500,1125)
widget.setWindowTitle('My window')
widget.show()
app.exec_()