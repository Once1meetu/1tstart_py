#Распознавание изображений с помощью глубоких сверточных нейронных сетей (ConvolutionalNeuralNetworks, CNN)

#Для начала установим необходимые библиотеки:

import tensorflow
import keras

#Затем загрузим набор данных MNIST, который содержит рукописные цифры от 0 до 9. Это стандартный наборданных для обучения моделей компьютерного зрения:

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Далее подготовим данные для использования в модели:

import numpy as np

# Приведем изображения к размеру 28x28 пикселей и нормализуем их значения от 0 до 1

x_train = np.reshape(x_train, (60000, 28, 28, 1)) / 255

x_test = np.reshape(x_test, (10000, 28, 28, 1)) / 255

# Кодируем метки классов в категории (one-hotencoding)

from keras.utils import to_categorical

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

#Теперь мы готовы создать модель нейронной сети:

from keras.models import Sequential

from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout

model = Sequential()

# Добавляем сверточные слои

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))

# Добавляем слои полносвязной нейронной сети

model.add(Flatten())

model.add(Dropout(0.5))

model.add(Dense(128, activation='relu'))

model.add(Dense(10, activation='softmax'))

#Обучим нашу модель на наборе данных MNIST:

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))

#Теперь, после обучения, мы можем проверить, насколько хорошо модель распознает рукописные цифры:

# Оценка точности модели на тестовом наборе данных

test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)