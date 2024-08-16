from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QFileDialog, QSizePolicy

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()
    def initUI(self):
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button_learn = QPushButton("Учить", self)
        self.button_learn.setObjectName("LearnButton")
        self.button_learn.clicked.connect(self.learn)

        self.button_load_image = QPushButton("Загрузить изображение", self)
        self.button_load_image.setObjectName("loadButton")
        self.button_load_image.clicked.connect(self.load_image)

        self.input_text = QLabel("Выберете свойство",self)
        self.input_text.setObjectName("LabelOfOptions")

        self.combo_box_position = QComboBox(self)
        self.combo_box_position.setObjectName("positionComboBox")
        self.combo_box_position.addItem("Летает")
        self.combo_box_position.addItem("Ездит на колёсах")
        self.combo_box_position.addItem("Мяукает")
        self.combo_box_position.addItem("Лает")
        self.combo_box_position.addItem("Квакает")
        self.combo_box_position.addItem("Имеет копыта")
        self.combo_box_position.addItem("Ходит по воде")

        self.button_add_text = QPushButton("Проверить", self)
        self.button_add_text.setObjectName("CheckButton")
        self.button_add_text.clicked.connect(self.check)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_learn)
        layout_buttons.addWidget(self.button_load_image)
        layout_buttons.addWidget(self.input_text)
        layout_buttons.addWidget(self.combo_box_position)
        layout_buttons.addWidget(self.button_add_text)
        layout.addLayout(layout_buttons)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QPushButton#loadButton,
            QPushButton#LearnButton,
            QPushButton#CheckButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }
            QLabel#LabelOfOptions {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }
        """)
    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение", "", "Изображения (*.png *.xpm *.jpg)")
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.path=image_path
    def learn(self):
        (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

        train_images = train_images / 255.0
        test_images = test_images / 255.0

        self.class_names = ['самолет', 'автомобиль', 'птица', 'кошка', 'олень', 'собака', 'лягушка', 'лошадь', 'корабль',
                       'грузовик']

        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(train_images, train_labels, epochs=1, batch_size=32, validation_split=0.2)
    def predict_img(self):
        img = Image.open(self.path).resize((32, 32)).convert('RGB')
        img_array = np.array(img) / 255.0
        self.predict = self.model.predict(img_array.reshape(1, 32, 32, 3))
        predicted_class = self.class_names[np.argmax(self.predict)]
        print('На картинке изображено:', predicted_class)
    def check(self):
        self.predict_img()
        position = self.combo_box_position.currentText()
        thing=np.argmax(self.predict)
        if ((thing==0 and position == "Летает") or
        (thing==1 and position == "Ездит на колёсах") or
        (thing == 2 and position == "Летает") or
        (thing == 3 and position == "Мяукает") or
        (thing == 4 and position == "Имеет копыта") or
        (thing == 5 and position == "Лает") or
        (thing == 6 and position == "Квакает") or
        (thing == 7 and position == "Имеет копыта") or
        (thing == 8 and position == "Ходит по воде") or
        (thing == 9 and position == "Ездит на колёсах")):
            self.input_text.setText("ПРАВИЛЬНО")
        else:
            self.input_text.setText("ОШИБКА")

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()