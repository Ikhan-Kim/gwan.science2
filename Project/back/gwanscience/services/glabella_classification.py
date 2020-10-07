import os
import PIL
from PIL import Image

import numpy as np
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# target_image
glabella_image_path = os.path.join(BASE_DIR, 'learning/classified/glabella_distance/test/big/283_eyebrow.jpg')

# test target_image
# glabella_image_path = os.path.join(BASE_DIR, 'learning/classified/glabella_distance/test/big/283_eyebrow.jpg')

image = tf.keras.preprocessing.image.load_img(
    glabella_image_path,
    grayscale=False,
    color_mode='rgb',
    target_size=(224,224), 
)

image_arr = tf.keras.preprocessing.image.img_to_array(image)
image = np.array([image_arr])/255.0

# glabella_distance
glabella_distance_model_path = os.path.join(BASE_DIR, 'learning/classified/training_glabella_distance_logs/model_glabella_distance4.h5')
glabella_distance_model = tf.keras.models.load_model(glabella_distance_model_path)

glabella_distance_classifications= glabella_distance_model.predict(image)
print(np.argmax(glabella_distance_classifications[0])) # 0: big, 1: mid, 2: small,