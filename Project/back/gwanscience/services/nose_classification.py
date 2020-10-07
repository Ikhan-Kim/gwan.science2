import os
import PIL
from PIL import Image

import numpy as np
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def predict(filename):
    # target_image
    nose_image_path = os.path.join(BASE_DIR, 'learning/classified/nose_length/test/mid/328_nose.jpg')

    # test target_image
    # nose_image_path = os.path.join(BASE_DIR, 'learning/classified/nose_width/train/small/6_nose.jpg')
    # nose_image_path = os.path.join(BASE_DIR, 'learning/classified/nose_length/test/big/324_nose.jpg')
    # eyes_image_path = os.path.join(BASE_DIR, 'learning/classified/eyes_distance/test/big/336_nose.jpg')

    image = tf.keras.preprocessing.image.load_img(
        nose_image_path,
        grayscale=False,
        color_mode='rgb',
        target_size=(224,224), 
    )

    image_arr = tf.keras.preprocessing.image.img_to_array(image)
    image = np.array([image_arr])/255.0

    # nose_length
    nose_length_model_path = os.path.join(BASE_DIR, 'services/learning/classified/training_nose_length_logs/model_nose_length2.h5')
    nose_length_model = tf.keras.models.load_model(nose_length_model_path)

    nose_length_classifications = nose_length_model.predict(image)
    # print(np.argmax(nose_length_classifications[0])) # 0: big, 1: mid, 2: small,
    nose_length = np.argmax(nose_length_classifications[0])


    # nose_width
    nose_width_model_path = os.path.join(BASE_DIR, 'services/learning/classified/training_nose_width_logs/model_nose_width2.h5')
    nose_width_model = tf.keras.models.load_model(nose_width_model_path)

    nose_width_classifications = nose_width_model.predict(image)
    # print(np.argmax(nose_width_classifications[0])) # 0: big, 1: mid, 2: small,
    nose_width = np.argmax(nose_width_classifications[0])

    data = [ nose_length, nose_width ]
    
    return data