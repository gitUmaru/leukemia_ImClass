import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
# This function will plot images in the form of a grid with 1 row and 5 columns where images are placed in each column.
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()



#train_image_generator = ImageDataGenerator(rescale=1./255)
#sample_training_images, _ = next(train_image_generator.flow_from_directory(batch_size=128,directory=os.path.abspath(r"biomedimaging_chall_DS\fold_1\fold_1"),shuffle=True,target_size=(150, 150),class_mode='binary'))
#plotImages(sample_training_images[:5])
