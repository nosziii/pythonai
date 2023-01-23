import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences  
import numpy

data = [("I am very happy today", 1), ("I am sad today", 0), ("I am excited about the concert", 1), 
        ("I am very angry with my boss", 0), ("I am content with my life", 1), 
        ("I am so bored at work", 0)]

train_data = data[:4]
test_data = data[4:]

tokenizer = Tokenizer()
texts = [d[0] for d in data]
tokenizer.fit_on_texts(texts)

train_texts = [d[0] for d in train_data]
train_texts = tokenizer.texts_to_sequences(train_texts)
train_texts = pad_sequences(train_texts, maxlen=20)



model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32, input_length=20),
    keras.layers.LSTM(64),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train_labels = [d[1] for d in train_data]
train_texts = numpy.array(train_texts)

model.fit(train_texts, train_labels, epochs=10)