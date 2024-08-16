#Прогнозирование временных рядов с помощью глубоких рекуррентных нейронных сетей (DeepRecurrentNeuralNetworks, DRNN)

#Для примера мы будем использовать набор данных "AirPassengers", который содержит данные о количестве авиапассажиров в течение нескольких лет.

import pandas as pd

import numpy as np

# Загрузка данных

data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv')

# Обработка данных

data['Month'] = pd.to_datetime(data['Month'])

data = data.set_index(['Month'])

data = data.astype('float32')

# Разбиение на тренировочный и тестовый наборы данных

train_data = data.iloc[:100, :]

test_data = data.iloc[100:, :]

#Затем мы можем подготовить данные для использования в модели:

# Функция для создания последовательностей из временных рядов

def create_sequences(data, sequence_length):
    X = []

    y = []

    for i in range(len(data) - sequence_length - 1):


seq = data[i:(i + sequence_length), :]

X.append(seq)

y.append(data[i + sequence_length, :])

return np.array(X), np.array(y)

# Определение длины последовательностей

sequence_length = 12

# Создание последовательностей для тренировочного набора данных

x_train, y_train = create_sequences(train_data.values, sequence_length)

# Создание последовательностей для тестового набора данных

x_test, y_test = create_sequences(test_data.values, sequence_length)

#Теперь мы готовы создать модель нейронной сети на основе рекуррентных слоев:

from keras.models import Sequential

from keras.layers import LSTM, Dense, Dropout

model = Sequential()

# Добавляем слои нейронной сети

model.add(LSTM(128, input_shape=(sequence_length, 1), return_sequences=True))

model.add(Dropout(0.2))

model.add(LSTM(64, return_sequences=True))

model.add(Dropout(0.2))

model.add(LSTM(32))

model.add(Dense(1))

# Компилируем модель

model.compile(loss='mean_squared_error', optimizer='adam')

#Обучим нашу модель на наборе данных "AirPassengers":

model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2)

#Теперь, после обучения, мы можем использовать нашу модель для прогнозирования временных рядов:

# Прогнозирование значений временных рядов

train_predict = model.predict(x_train)

test_predict = model.predict(x_test)

# Обработка результатов

train_predict = np.concatenate((train_predict, np.zeros((len(train_data) - len(train_predict), 1))))

test_predict = np.concatenate((test_predict, np.zeros((len(test_data) - len(test_predict), 1))))

# Визуализация результатов

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))­­­

plt.plot(data.values, label='Исходныеданные')

plt.plot(train_predict, label='Прогнознатренировочныхданных')

plt.plot(test_predict, label='Прогнознатестовыхданных')

plt.legend()

plt.show()