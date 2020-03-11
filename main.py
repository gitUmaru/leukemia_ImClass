import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os

np.set_printoptions(suppress=True)

path  = os.path.abspath("biomedimaging_chall_DS\keras_model.h5")
image_path = os.path.abspath(r"biomedimaging_chall_DS\fold_1\fold_1\hem\UID_H10_14_1_hem.bmp")

model = tensorflow.keras.models.load_model(path)
    #Trained on home PC, will transfer train.py and etc later via gitHub repo

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open(image_path)

size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

image_array = np.asarray(image)

image.show()

normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

data[0] = normalized_image_array

prediction = model.predict(data)
print(prediction)
