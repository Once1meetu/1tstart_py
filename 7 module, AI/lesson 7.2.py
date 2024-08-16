import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

(train_images, train_labels),(test_images,test_labels)=datasets.cifar10.load_data()

train_images=train_images/255.0
test_images=test_images/255.0

class_names =['самолет','автомобиль','птица','кошка','олень','собака','лягушка','лошадь','корабль','грузовик']

model=models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=1, batch_size=32,validation_split=0.2)

def predict_img(img_path):
    img=Image.open(img_path).resize((32,32)).convert('RGB')
    img_array=np.array(img)/255.0
    plt.imshow(img_array, cmap=plt.cm.binary)
    plt.show()
    predict=model.predict(img_array.reshape(1,32,32,3))
    predicted_class=class_names[np.argmax(predict)]
    print('predict:',predicted_class)

predict_img(r"D:\1tstart78\neural_networks\72\cat.jpg")
predict_img("dog.jpg")