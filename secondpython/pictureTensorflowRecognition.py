import tensorflow as tf
from tensorflow import keras
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Betöltjük a mentett modellt
loaded_model = keras.models.load_model('my_model.h5')

# Betöltjük a teszt képet
img = Image.open('test_dog.jpg')
img = img.resize((32,32))
img_arr = np.array(img)
img_arr = img_arr/255.0
img_arr = np.expand_dims(img_arr, axis=0)



# Előrejelzés
predictions = loaded_model.predict(img_arr)

# A legnagyobb indexű oszlop a valószínűbb kategória
# predicted_class = np.argmax(predictions[0])

# Megjelenítjük a képet és a predikciót
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
predicted_class = class_names[np.argmax(predictions[0])]
plt.imshow(img)
plt.title(f'Predicted class: {predicted_class}')
plt.show()

