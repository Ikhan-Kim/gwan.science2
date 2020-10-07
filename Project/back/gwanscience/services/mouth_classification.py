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
# mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/lips_length/test/big/316_mouse.jpg')

# test target_image
# mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/lips_length/test/big/320_mouse.jpg')
# mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/lips_length/train/small/90_mouse.jpg')

# mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/lips_thickness/test/big/280_mouse.jpg')
# mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/lips_thickness/train/big/1_mouse.jpg')

mouth_image_path = os.path.join(BASE_DIR, 'learning/classified/mouth_tail/test/down/334_mouse.jpg')

image = tf.keras.preprocessing.image.load_img(
    mouth_image_path,
    grayscale=False,
    color_mode='rgb',
    target_size=(224,224), 
)

image_arr = tf.keras.preprocessing.image.img_to_array(image)
image = np.array([image_arr])/255.0

# lips_length
lips_length_model_path = os.path.join(BASE_DIR, 'learning/classified/training_lips_length_logs/model_lips_length5.h5')
lips_length_model = tf.keras.models.load_model(lips_length_model_path)

lips_length_classifications = lips_length_model.predict(image)
print(np.argmax(lips_length_classifications[0])) # 0: big, 1: mid, 2: small,



# lips_thickness
lips_thickness_model_path = os.path.join(BASE_DIR, 'learning/classified/training_lips_thickness_logs/model_lips_thickness1.h5')
lips_thickness_model = tf.keras.models.load_model(lips_thickness_model_path)

lips_thickness_classifications = lips_thickness_model.predict(image)
print(np.argmax(lips_thickness_classifications[0])) # 0: big, 1: mid, 2: small,


# mouth_tail
mouth_tail_model_path = os.path.join(BASE_DIR, 'learning/classified/training_mouth_tail_logs/model_mouth_tail6.h5')
mouth_tail_model = tf.keras.models.load_model(mouth_tail_model_path)

image_tail = tf.keras.preprocessing.image.load_img(
    mouth_image_path,
    grayscale=False,
    color_mode='rgb',
    target_size=(200,200), 
)

image_tail_arr = tf.keras.preprocessing.image.img_to_array(image_tail)
image_tail = np.array([image_tail_arr])/255.0

mouth_tail_classifications = mouth_tail_model.predict(image_tail)
print(np.argmax(mouth_tail_classifications[0])) # 0: down, 1: mid, 2: up,