# README

## 사용된 Matplotlib 해석

```python
import matplotlib.pyplot as plt
```

```python
plt.figure() # figure 생성
plt.imshow(image) # 이미지 출력
plt.colobar() # RGB 컬러바
plt.grid(False) # 눈금선 표시 여부
plt.show() # 시각화
```

```python
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1) # 가로 5등분 세로 5등분 후 i+1 번째 칸에 출력
    plt.xticks([]) # x축 눈금 값 설정(예시와 같이 빈 배열로 지정하면 눈금이 제거됨)
    plt.yticks([]) # y축 눈금 값 설정
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
```

```python
def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777") # bar: 막대그래프
  plt.ylim([0, 1]) # y축 범위 제한
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
```





# 케라스를 이용한 딥러닝 모델링

## 순서

1. 데이터셋 생성하기

   - 원본 데이터를 불러오거나 시뮬레이션을 통해 데이터를 생성합니다.
   - 데이터로부터 훈련셋, 검증셋, 시험셋을 생성합니다.
   - 이 때 딥러닝 모델의 학습 및 평가를 할 수 있도록 포맷 변환을 합니다.

2. 모델 구성하기

   - 시퀀스 모델을 생성한 뒤 필요한 레이어를 추가하여 구성합니다.
   - 좀 더 복잡한 모델이 필요할 때는 케라스 함수 API를 사용합니다.

3. 모델 학습과정 설정하기

   - 학습하기 전에 학습에 대한 설정을 수행합니다.
   - 손실 함수 및 최적화 방법을 정의합니다.
   - 케라스에서는 compile() 함수를 사용합니다.

4. 모델 학습시키기

   - 훈련셋을 이용하여 구성한 모델로 학습시킵니다.
   - 케라스에서는 fit() 함수를 사용합니다.

5. 학습과정 살펴보기

   - 모델 학습 시 훈련셋, 검증셋의 손실 및 정확도를 측정합니다.
   - 반복횟수에 따른 손실 및 정확도 추이를 보면서 학습 상황을 판단합니다.

6. 모델 평가하기

   - 준비된 시험셋으로 학습한 모델을 평가합니다.
   - 케라스에서는 evaluate() 함수를 사용합니다.

7. 모델 사용하기

   - 임의의 입력으로 모델의 출력을 얻습니다.
   - 케라스에서는 predict() 함수를 사용합니다.

   

## 모델 작성법

[참고자료](https://tykimos.github.io/2017/01/27/CNN_Layer_Talk/)

### 모델 정의

```python
# 모델 예시1
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# 위와 동일한 코드
# 아래와 같이 add를 이용하면 정의된 후에 층을 추가할 수도 있다.
model = keras.Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

#### Flatten()

인풋을 일렬화 합니다. 배치 크기에는 영향을 주지 않습니다.

예시1에서는 2차원 배열(28 x 28 픽셀)의 이미지 포맷을 28 * 28 = 784 픽셀의 1차원 배열로 변환합니다.

#### Dense()

보통의 밀집 연결 신경망 레이어.

- **units**: 양의 정수, 아웃풋 공간의 차원. (예시1의 첫 번째 인자)
- **activation**: 사용할 활성화 함수를 설정. 참고 : [활성화](https://keras.io/ko/activations/)
  - 'relu' : 은닉층에 주로 쓰임
  - 'softmax' : 소프트맥스 함수, 다중 클래스 분류 문제에서 출력층에 주로 쓰임

```python
# 모델 예시2
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

```

#### Conv2D()

- 첫번째 인자(**filters**) : 컨볼루션 필터의 수 입니다.
- 두번째 인자(**kernel_size**) : 컨볼루션 커널의 크기 입니다. `(n, n)`과 같이 튜플형식으로 입력 가능
- **activation** : 활성화 함수 설정합니다. 참고 : [활성화](https://keras.io/ko/activations/)
  - ‘relu’ : 은닉층에 주로 쓰임

#### MaxPooling2D()

컨볼루션 레이어의 출력 이미지에서 주요값만 뽑아 크기가 작은 출력 영상을 만듭니다. 이것은 지역적인 사소한 변화가 영향을 미치지 않도록 합니다.	



### 모델 컴파일

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

- 손실 함수 (loss function) : 훈련 하는 동안 모델의 오차를 측정. `categorical_crossentropy` 또는 `mse`와 같은 기존의 손실 함수의 문자열 식별자 또는 목적 함수를 사용할 수 있습니다. 참고: [손실](https://keras.io/losses)
- 정규화하기 (optimizer) :  데이터와 손실 함수를 바탕으로 모델의 업데이트 방법을 결정, `rmsprp`나 `adagrad`와 같은 기존의 정규화기에 대한 문자열 식별자 또는 `Optimizer` 클래스의 인스턴스를 사용할 수 있습니다. 참고: [정규화](https://keras.io/optimizers)
- 지표(metric) :  위의 예에서는 올바르게 분류된 이미지의 비율인 *정확도(accuracy)*를 사용합니다.



## 모델 훈련 및 정확도 평가

### batch size와 epoch

`batch size`란 sample데이터 중 한번에 네트워크에 넘겨주는 데이터 수를 말한다.

`epoch`는 한번의 훈련(training)을 말한다.

예를 들어 1000의 데이터를 batch_size = 10 으로 넘겨준다고 가정하면

1epoch = 10(batch_size) * 100(step)

즉, batch_size가 커지면 한번에 많은량을 학습하기 때문에 train과정이 빨라질수 있으나 컴퓨터의 메모리 문제 때문에 나눠서 하는 것이다.

```python
# 모델 훈련 예시
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=3
)
# 예시2
model.fit(
    train_ds,
    train2_ds,
    validation_data=(val_ds, val2_ds),
    epochs=3,
    batch_size=10
)
```

batch_sized의 default 값은 32 이다.

훈련하는동안 epoch 단위로 손실률(loss), 정확도(accuracy) 등의 정보가 출력된다.

### 정확도 평가

```python
test_loss, test_acc = model.evaluate(test_ds, verbose=2)

print('\n테스트 정확도:', test_acc)
```

model.evaluate() 함수는 손실과 정확도를 반환한다.



## 학습된 모델 저장 및 불러오기

```python
from keras.models import load_model

model.save('file_name') # 저장
model = load_model('file_name') # 불러오기
```



## 모델 예측 만들기

```python
# 1.Basic_image_classification.py 참고

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 값의 범위를 0~1 사이로 조정
train_images = train_images / 255.0
test_images = test_images / 255.0

### 모델 생성, 컴파일, 훈련 생략 ###

# 예측 만들기
predictions = model.predict(test_images)
predictions[0]
np.argmax(predictions[0])
test_labels[0]

# 테스트 세트에서 이미지 하나를 선택
img = test_images[0]
img.shape # (28, 28)

# tf.keras 모델은 한 번에 샘플의 묶음 또는 배치(batch)로 예측을 만드는데 최적화되어 있다. 하나의 이미지를 사용할 때에도 2차원 배열로 만들어야 합니다:
img = (np.expand_dims(img,0))
img.shape # (1, 28, 28)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# 이미지 예측 만들기
predictions_single = model.predict(img)
plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
```

