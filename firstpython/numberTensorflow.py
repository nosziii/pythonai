import tensorflow as tf
from tensorflow import keras

# Betöltjük a MNIST adatbázist
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Átalakítjuk az adatokat, hogy azokat a hálózat elfogadja
x_train = x_train / 255.0
x_test = x_test / 255.0

# Létrehozunk egy egyszerű neurális hálózatot
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Kompiláljuk a modellt
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Tanítjuk a modellt az adatokkal
model.fit(x_train, y_train, epochs=5)

# Ellenőrizzük a modell pontosságát a tesztadatokkal
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)