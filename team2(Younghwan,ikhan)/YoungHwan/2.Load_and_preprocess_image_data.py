# 참고 : https://www.tensorflow.org/tutorials/load_data/images

# 이미지 로드

import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds

import matplotlib.pyplot as plt
from tensorflow.keras import layers


# 꽃 데이터셋 다운로드
# ※ 모든 이미지는 CC-BY 라이선스가 부여되며 제작자는 LICENSE.txt 파일에 나열됩니다. ※

import pathlib
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url, 
                                   fname='flower_photos', 
                                   untar=True)
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg'))) # 3670


# keras.preprocessing을 사용하여로드
# image_dataset_from_directory를 사용하여 이러한 이미지를 디스크에서로드 해 보겠습니다.

# 데이터셋 만들기
batch_size = 32
img_height = 180
img_width = 180

# 이미지의 80 %를 훈련에 사용하고 20 %를 유효성 검사에 사용합니다.
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# 이러한 데이터 세트의 class_names 속성에서 클래스 이름을 찾을 수 있습니다.
class_names = train_ds.class_names
print(class_names)


# # 데이터 시각화
# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()

for image_batch, labels_batch in train_ds:
  print(image_batch.shape) # (32, 180, 180, 3)
  print(labels_batch.shape) # (32,)
  break
"""
image_batch 는 (32, 180, 180, 3) 모양의 텐서입니다.
이것은 180x180x3 모양의 32 개 이미지의 배치입니다 (마지막 치수는 색상 채널 RGB 참조).
label_batch 는 (32,) 모양의 텐서이며 32 개의 이미지에 해당하는 레이블입니다.
"""


# 데이터 표준화
"""
RGB 채널 값은 [0, 255] 범위에 있습니다. 이것은 신경망에 이상적이지 않습니다. 일반적으로 입력 값을 작게 만들어야합니다.
여기서는 Rescaling 레이어를 사용하여 [0, 1] 에있는 값을 표준화합니다.
"""
normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
print(np.min(first_image), np.max(first_image)) 


# 성능을 위한 데이터셋 구성
"""
I / O가 차단되지 않고 디스크에서 데이터를 생성 할 수 있도록 버퍼링 된 프리 페칭을 사용해야합니다.
다음은 데이터를로드 할 때 사용해야하는 두 가지 중요한 방법입니다.

.cache() 는 첫 번째 에포크 동안 디스크에서로드 된 이미지를 메모리에 보관합니다.
이렇게하면 모델을 학습하는 동안 데이터 세트가 병목 현상이 발생하지 않습니다.
데이터 세트가 너무 커서 메모리에 맞지 않는 경우이 방법을 사용하여 고성능 온 디스크 캐시를 만들 수도 있습니다.

.prefetch() 학습 중에 데이터 전처리 및 모델 실행과 겹칩니다.
"""
AUTOTUNE = tf.data.experimental.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


# 모델 작성
num_classes = 5

model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])


# 모델 컴파일
model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

# model.summary()

# 모델 훈련
epochs=10
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)


# 훈련 결과 시각화
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss=history.history['loss']
val_loss=history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()