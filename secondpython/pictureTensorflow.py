import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Betöltjük a Cifar10 adatbázist
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# Átalakítjuk az adatokat, hogy azokat a hálózat elfogadja
x_train = x_train / 255.0
x_test = x_test / 255.0


# Létrehozunk egy neurális hálózatot
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Kompiláljuk a modellt
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Tanítjuk a modellt az adatokkal, és elmentjük a pontossági és a veszteség értékeket
history = model.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test))

# Ellenőrizzük a modell pontosságát a tesztadatokkal
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# Megjelenítjük a tanítási folyamatot grafikusan
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

model.save('my_model.h5')
