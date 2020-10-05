import os
import PIL
from PIL import Image
from django.conf import settings

import numpy as np
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

LEARN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

train_dir = os.path.join(LEARN_DIR, 'lips_length/train')
val_dir = os.path.join(LEARN_DIR, 'lips_length/validation')

# label
training_datagen = ImageDataGenerator(rescale = 1./255)
validation_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = training_datagen.flow_from_directory(
	train_dir,
	target_size=(224, 224),
	class_mode='categorical',
    batch_size= 16
)

validation_generator = validation_datagen.flow_from_directory(
	val_dir,
	target_size=(224, 224),
	class_mode='categorical',
    batch_size= 16
)

# define model
model = tf.keras.models.Sequential([
    #1
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    #2
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    #3
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    #4
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    #5
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    #6
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# model.compile(loss = 'categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

checkpoint_path = os.path.join(LEARN_DIR, 'training_lips_length_logs/cp-4-{epoch:04d}.ckpt')
checkpoint_dir = os.path.dirname(checkpoint_path)

ckpt_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1, period=100)

history = model.fit(train_generator, epochs=500, steps_per_epoch=8, validation_data = validation_generator, verbose = 1, validation_steps=3, callbacks=[ckpt_callback])

# model.save("model_eyes_size.h5")

save_path = os.path.join(LEARN_DIR,'training_lips_length_logs/model_lips_length5.h5')
model.save(save_path)

# 정확도 그래프
import matplotlib.pyplot as plt
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Lips_length Training and validation accuracy')
plt.legend(loc=0)
plt.figure()

plt.show()
