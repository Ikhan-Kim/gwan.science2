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

