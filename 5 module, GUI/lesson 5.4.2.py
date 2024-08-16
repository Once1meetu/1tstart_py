from PyQt5.QtCore import Qt, QRect

from PyQt5.QtGui import QPixmap, QPainter, QFont

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QFileDialog, QSizePolicy

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Мое приложение")

        self.setGeometry(100, 100, 500, 400)

        self.initUI()

    def initUI(self):

        # Создание виджетов

        self.image_label = QLabel(self)

        self.image_label.setAlignment(Qt.AlignCenter)

        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button_load_image = QPushButton("Загрузить изображение", self)

        self.button_load_image.setObjectName("loadButton")

        self.button_load_image.clicked.connect(self.load_image)

        self.input_text = QLineEdit(self)

        self.input_text.setObjectName("inputField")

        self.combo_box_position = QComboBox(self)

        self.combo_box_position.setObjectName("positionComboBox")

        self.combo_box_position.addItem("Верхний левый угол")

        self.combo_box_position.addItem("Верхний правый угол")

        self.combo_box_position.addItem("Нижний левый угол")

        self.combo_box_position.addItem("Нижний правый угол")

        self.combo_box_position.addItem("По центру")

        self.button_add_text = QPushButton("Добавить текст", self)

        self.button_add_text.setObjectName("addTextButton")

        self.button_add_text.clicked.connect(self.add_text)

        # Размещение виджетов с помощью менеджера компоновки

        layout = QVBoxLayout()

        layout.addWidget(self.image_label)

        layout_buttons = QHBoxLayout()

        layout_buttons.addWidget(self.button_load_image)

        layout_buttons.addWidget(self.input_text)

        layout_buttons.addWidget(self.combo_box_position)

        layout_buttons.addWidget(self.button_add_text)

        layout.addLayout(layout_buttons)

        central_widget = QWidget()

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        # Применение стилей

        self.setStyleSheet("""

            QMainWindow {

                background-color: #F0F0F0;

            }

            QPushButton#loadButton,

            QPushButton#addTextButton {

                background-color: #4CAF50;

                color: white;

                border: none;

                padding: 10px 20px;

                font-size: 16px;

            }

            QLineEdit#inputField {

                border: 2px solid #4CAF50;

                border-radius: 5px;

                padding: 5px;

                font-size: 16px;

            }

        """)

    def load_image(self):

        # Загрузка изображения

        file_dialog = QFileDialog()

        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение", "", "Изображения (*.png *.xpm *.jpg)")

        pixmap = QPixmap(image_path)

        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def add_text(self):

        # Получение введенного текста и выбранной позиции

        text = self.input_text.text()

        position = self.combo_box_position.currentText()

        if text:

            # Получение текущего изображения

            pixmap = self.image_label.pixmap()

            # Настройка шрифта и позиции в зависимости от выбранной позиции

            font = QFont("Arial", 20)

            rect = QRect(0, 0, pixmap.width(), pixmap.height())

            if position == "Верхний левый угол":

                align_flag = Qt.AlignTop | Qt.AlignLeft

            elif position == "Верхний правый угол":

                align_flag = Qt.AlignTop | Qt.AlignRight

            elif position == "Нижний левый угол":

                align_flag = Qt.AlignBottom | Qt.AlignLeft

            elif position == "Нижний правый угол":

                align_flag = Qt.AlignBottom | Qt.AlignRight

            else:

                align_flag = Qt.AlignCenter

            # Создание QPainter для рисования текста на изображении

            painter = QPainter(pixmap)

            painter.setFont(font)

            painter.drawText(rect, align_flag, text)

            painter.end()

            # Отображение обновленного изображения

            self.image_label.setPixmap(pixmap)

app = QApplication([])

window = MainWindow()

window.show()

app.exec_()