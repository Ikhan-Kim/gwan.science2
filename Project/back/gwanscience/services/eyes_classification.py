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
    # eyes_image_path = os.path.join(BASE_DIR, 'learning/classified/eyes_size/test/big/273_eye.jpg')
    eyes_image_path = os.path.join(BASE_DIR, 'media/split/'+str(filename) +'_eyes.jpg')

    # test target_image
    # eyes_image_path = os.path.join(BASE_DIR, 'learning/classified/eyes_size/test/big/273_eye.jpg')
    # eyes_image_path = os.path.join(BASE_DIR, 'learning/classified/eyes_tail/test/mid/307_eye.jpg')
    # eyes_image_path = os.path.join(BASE_DIR, 'learning/classified/eyes_distance/test/big/336_eye.jpg')

    image = tf.keras.preprocessing.image.load_img(
        eyes_image_path,
        grayscale=False,
        color_mode='rgb',
        target_size=(224,224), 
    )

    image_arr = tf.keras.preprocessing.image.img_to_array(image)
    image = np.array([image_arr])/255.0

    # eyes_size
    eyes_size_model_path = os.path.join(BASE_DIR, 'services/learning/classified/training_eyes_size_logs/model_eyes_size3.h5')
    eyes_size_model = tf.keras.models.load_model(eyes_size_model_path)

    eyes_size_classifications = eyes_size_model.predict(image)
    # print(np.argmax(eyes_size_classifications[0])) # 0: big, 1: mid, 2: small,
    eyes_size = np.argmax(eyes_size_classifications[0])



    # eyes_tail
    eyes_tail_model_path = os.path.join(BASE_DIR, 'services/learning/classified/training_eyes_tail_logs/model_eyes_tail1.h5')
    eyes_tail_model = tf.keras.models.load_model(eyes_tail_model_path)

    eyes_tail_classifications = eyes_tail_model.predict(image)
    # print(np.argmax(eyes_tail_classifications[0])) # 0: down, 1: mid, 2: up,
    eyes_tail = np.argmax(eyes_tail_classifications[0])

    # eyes_distance
    eyes_distance_model_path = os.path.join(BASE_DIR, 'services/learning/classified/training_eyes_distance_logs/model_eyes_distance1.h5')
    eyes_distance_model = tf.keras.models.load_model(eyes_distance_model_path)

    eyes_distance_classifications = eyes_distance_model.predict(image)
    # print(np.argmax(eyes_distance_classifications[0])) # 0: big, 1: mid, 2: small,
    eyes_distance = np.argmax(eyes_distance_classifications[0])

    data = [ eyes_size, eyes_tail, eyes_distance ]

    return data