# 참고 : https://www.tensorflow.org/tutorials/keras/save_and_load

# 모델 저장과 복원
"""
훈련하는 도중이나 훈련이 끝난 후에 모델을 저장할 수 있습니다.
모델을 중지된 지점부터 다시 훈련할 수 있어 한 번에 오랫동안 훈련하지 않아도 됩니다.
또 모델을 저장하면 다른 사람에게 공유할 수 있고 작업을 재현할 수 있습니다.
"""

# 저장 방식
# 사용하는 API에 따라서 여러가지 방법으로 텐서플로 모델을 저장할 수 있습니다. 이 문서는 텐서플로 모델을 만들고 훈련하기 위한 고수준 API인 tf.keras를 사용합니다.

# pip install -q pyyaml h5py  # HDF5 포맷으로 모델을 저장하기 위해서 필요합니다
import os

import tensorflow as tf
from tensorflow import keras


# 예제 데이터셋 받기
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0


# 모델 정의
# 간단한 Sequential 모델을 정의합니다
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

  return model

# 모델 객체를 만듭니다
model = create_model()

# 모델 구조를 출력합니다
model.summary()


# 훈련하는 동안 체크포인트 저장하기
"""
훈련 중간과 훈련 마지막에 체크포인트(checkpoint)를 자동으로 저장하도록 하는 것이 많이 사용하는 방법입니다.
다시 훈련하지 않고 모델을 재사용하거나 훈련 과정이 중지된 경우 이어서 훈련을 진행할 수 있습니다.
tf.keras.callbacks.ModelCheckpoint은 이런 작업을 수행하는 콜백(callback)입니다.
이 콜백은 체크포인트 작업을 조정할 수 있도록 여러가지 매개변수를 제공합니다.
"""

# 체크포인트 콜백 사용하기
checkpoint_path = "checkpoints/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# 모델의 가중치를 저장하는 콜백 만들기
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True, # 가중치만 저장
                                                 verbose=1)
                                                 # period=n : n번째 에포트마다 저장 

# 새로운 콜백으로 모델 훈련하기
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # 콜백을 훈련에 전달합니다

# 옵티마이저의 상태를 저장하는 것과 관련되어 경고가 발생할 수 있습니다.
# 이 경고는 (그리고 이 노트북의 다른 비슷한 경고는) 이전 사용 방식을 권장하지 않기 위함이며 무시해도 좋습니다.

# 이 코드는 텐서플로 체크포인트 파일을 만들고 에포크가 종료될 때마다 업데이트합니다.


"""
훈련하지 않은 새로운 모델을 만들어 보겠습니다.
가중치만 복원할 땐 원본 모델과 동일한 구조로 모델을 만들어야 합니다.
여기서는 동일한 구조로 모델을 만들었으므로 다른 객체이지만 가중치를 공유할 수 있습니다.

훈련하지 않은 새 모델을 만들고 테스트 세트에서 평가해 보죠. 훈련되지 않은 모델의 성능은 무작위로 선택하는 정도의 수준입니다(~10% 정확도):
"""
model = create_model()

# 모델을 평가합니다
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("훈련되지 않은 모델의 정확도: {:5.2f}%".format(100*acc))

# 가중치 로드
model.load_weights(checkpoint_path)

# 모델 재평가
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc)) 




# 전체 모델 저장하기
# 두 개의 포맷(SavedModel과 HDF5)으로 모델을 저장할 수 있습니다.

# 1. SavedModel 포맷
# 새로운 모델 객체를 만들고 훈련합니다
model = create_model()
model.fit(train_images, train_labels, epochs=5)

# SavedModel로 전체 모델을 저장합니다
# mkdir saved_models
model.save('saved_models/my_model') 

# 저장된 모델로부터 새로운 케라스 모델을 로드합니다:
new_model = tf.keras.models.load_model('saved_models/my_model')

# 모델 구조를 확인
new_model.summary()


# 2. HDF5 파일로 저장하기
# 새로운 모델 객체를 만들고 훈련합니다
model = create_model()
model.fit(train_images, train_labels, epochs=5)

# 전체 모델을 HDF5 파일로 저장합니다
# '.h5' 확장자는 이 모델이 HDF5로 저장되었다는 것을 나타냅니다
model.save('saved_models/my_model.h5') 

# 가중치와 옵티마이저를 포함하여 정확히 동일한 모델을 다시 생성합니다
new_model = tf.keras.models.load_model('saved_models/my_model.h5')

# 모델 구조를 출력합니다
new_model.summary()