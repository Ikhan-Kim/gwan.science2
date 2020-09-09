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
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
```



## 모델 작성법 학습

### 모델 정의

[Keras Docs >> layers >> Core Layers](https://keras.io/ko/layers/core/)

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), # 2차원 배열(28 x 28 픽셀)의 이미지 포맷을 28 * 28 = 784 픽셀의 1차원 배열로 변환
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

#### Flatten

인풋을 일렬화 합니다. 배치 크기에는 영향을 주지 않습니다.

#### Dense

보통의 밀집 연결 신경망 레이어.

- **units**: 양의 정수, 아웃풋 공간의 차원. (예시의 첫 번째 인자)
- **activation**: 사용할 활성화 함수 ([활성화](https://keras.io/ko/activations/)를 참조하십시오). 따로 정하지 않으면, 활성화가 적용되지 않습니다. (다시 말해, "선형적" 활성화: `a(x) = x`).

### 모델 컴파일

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

- 손실 함수 (loss function) : 훈련 하는 동안 모델의 오차를 측정. `categorical_crossentropy` 또는 `mse`와 같은 기존의 손실 함수의 문자열 식별자 또는 목적 함수를 사용할 수 있습니다. 참고: [손실](https://keras.io/losses)
- 정규화하기 (optimizer) :  데이터와 손실 함수를 바탕으로 모델의 업데이트 방법을 결정, `rmsprp`나 `adagrad`와 같은 기존의 정규화기에 대한 문자열 식별자 또는 `Optimizer` 클래스의 인스턴스를 사용할 수 있습니다. 참고: [정규화](https://keras.io/optimizers)
- 지표(metric) :  위의 예에서는 올바르게 분류된 이미지의 비율인 *정확도(accuracy)*를 사용합니다.