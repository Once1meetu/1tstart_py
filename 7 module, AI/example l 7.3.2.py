#Анализ текстов и предсказание тональности с помощью рекуррентных нейронных сетей (RNN)

#Для начала установим необходимые библиотеки:

Import
nltk

#Затем загрузим и подготовим набор данных IMDB, который содержит отзывы пользователей о фильмах и их оценки (положительные или отрицательные):

from keras.datasets import imdb

from keras.preprocessing.sequence import pad_sequences

vocab_size = 20000

sequence_length = 100

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# Заполняем последовательности нулями или обрезаем их до определенной длины

x_train = pad_sequences(x_train, maxlen=sequence_length)

x_test = pad_sequences(x_test, maxlen=sequence_length)

#Теперь мы готовы создать модель нейронной сети на основе рекуррентных слоев:

from keras.models import Sequential

from keras.layers import Embedding, LSTM, Dense

model = Sequential()

# Добавляем слои нейронной сети

model.add(Embedding(vocab_size, 128, input_length=sequence_length))

model.add(LSTM(64, return_sequences=True))

model.add(LSTM(32))

model.add(Dense(1, activation='sigmoid'))

#Обучим нашу модель на наборе данных IMDB:

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))

#Теперь, после обучения, мы можем проверить, насколько хорошо модель предсказывает тональность отзывов:

# Оценка точности модели на тестовом наборе данных

test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)