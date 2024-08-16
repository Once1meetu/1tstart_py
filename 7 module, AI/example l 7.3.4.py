#Классификация и детектирование спама в электронных сообщениях с помощью многослойных персептронов (MultilayerPerceptron, MLP)

#Для начала установим необходимые библиотеки:
import scikit-learn
#Загрузим и подготовим набор данных Spam для обучения модели:
import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split

from keras.utils import to_categorical

from keras.preprocessing.text import Tokenizer

from keras.preprocessing.sequence import pad_sequences

# Загрузка данных

data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/spam.csv',

                   encoding='latin-1')

data = data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)

data = data.rename(columns={'v1': 'target', 'v2': 'text'})

# Обработка данных

target = data.pop('target').values

text = data.pop('text').values

tokenizer = Tokenizer(num_words=5000)

tokenizer.fit_on_texts(text)

text = tokenizer.texts_to_sequences(text)

text = pad_sequences(text, maxlen=100)

target = to_categorical(target, num_classes=2)

# Разбивка на тренировочный и тестовый наборы данных

x_train, x_test, y_train, y_test = train_test_split(text, target, test_size=0.2)
#Теперь мы готовы создать многослойный персептрон для классификации электронных сообщений:
from keras.models import Sequential

from keras.layers import Dense, Dropout

model = Sequential()

# Добавляем слои персептрона

model.add(Dense(128, input_dim=x_train.shape[1], activation='relu'))

model.add(Dropout(0.2))

model.add(Dense(64, activation='relu'))

model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

# Компилируем модель

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#Обучим нашу модель на наборе данных Spam:
model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2, validation_data=(x_test, y_test))
#Теперь, после обучения, мы можем проверить, насколько хорошо модель классифицирует электронные сообщения на спам и не спам:
# Оценка точности модели на тестовом наборе данных

test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)