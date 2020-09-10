# 참고 : https://www.tensorflow.org/tutorials/images/data_augmentation


# 데이터 증대(augmentation)


# 개요
# 이 튜토리얼은 이미지 회전과 같은 변환을 적용하여 훈련 세트의 다양성을 증가시키는 기술인 데이터 증가를 보여줍니다.

# pip install -q tf-nightly

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

# 2에서 사용한 꽃 데이터셋
(train_ds, val_ds, test_ds), metadata = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
)
get_label_name = metadata.features['label'].int2str

image, label = next(iter(train_ds))


# 크기 조정(Resizing and rescaling)
IMG_SIZE = 180

resize_and_rescale = tf.keras.Sequential([
  layers.experimental.preprocessing.Resizing(IMG_SIZE, IMG_SIZE), # Resizing : 가로 세로 사이즈를 지정
  layers.experimental.preprocessing.Rescaling(1./255) # Rescaling : 픽셀 배율 조정
])


# 데이터 증대
# 데이터 증대에도 전처리 레이어를 사용할 수 있습니다.

# 몇 개의 전처리 레이어를 만들어 동일한 이미지에 반복적으로 적용 해 보겠습니다.
data_augmentation = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
  layers.experimental.preprocessing.RandomRotation(0.2),
])

# Add the image to a batch
image = tf.expand_dims(image, 0)

plt.figure(figsize=(10, 10))
for i in range(9):
  augmented_image = data_augmentation(image)
  ax = plt.subplot(3, 3, i + 1)
  plt.imshow(augmented_image[0])
  plt.axis("off")
plt.show()


# tf.image 사용 (참고 : https://www.tensorflow.org/api_docs/python/tf/image)
# 이미지 뒤집기
flipped = tf.image.flip_left_right(image)
# 이미지 90도 회전
rotated = tf.image.rot90(image)

# tf.image를 사용하면 이미지 데이터를 위의 예시 말고도 더 많이 증대시킬수 있습니다.