# Matplotilb 기본 사용법

- 다양한 데이터를 시각화할 수 있도록 도와주는 라이브러리입니다.
- 간단한 데이터 분석에서부터 인공지능 모델의 시각화까지 활용도가 매우 높습니다.

### 그래프 그리기, 저장하기

``` python
import matplotlib.pyplot as plt
import numpy as np

# 직선 그래프 그리기
x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x,y)
plt.title("My plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 그래프 저장하기
plt.savefig('Myplot.png') #matplotlib라이브러리에 savefig가 저장되어있음

# 여러 그래프 같이 저장하기
x = np.linspace(0, np.pi * 10, 500) # pi*10배 너비에, 500개의 점을 균일하게 찍기
fig, axes = plt.subplot(2,1) # 2개의 그래프가 들어가는 Figure 생성
axes[0].plot(x, np.sin(x)) # 첫 번째 그래프 sin 그래프
axes[1].plot(x, np.cos(x)) # 두 번째 그래프 cos 그래프
fig.savefig("sin&cos.png")

선 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
y = x ** 2

plt.plot(x,y)
plt.show()
```



### 선 그래프 그리기

``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
y = x ** 2

plt.plot(x,y)
plt.show()
# 라인 스타일로 "-", ":", ":", "-", "--" 등이 사용가능
plt.plot(x, y, linestyle=":", marker="*")
# X축 및 Y축에서 특정 범위를 자를 수 있다.
plt.show()
```



### 하나의 그래프에 2개의 선 넣기, legend 삽입하기

``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
y1 = x ** 2
y2 = -x

#하나의 그래프에 2개 선 넣기
plt.plot(x, y1, linestyle="-", marker="*", color="red", label="y = x*x")
plt.plot(x, y2, linestyle=":", marker="o", color="blue", label="y = -x")
plt.xlabel("X")
plt.ylabel("Y")
#legned 삽입하기
plt.legend(
	shadow=True, #legend에 음영주기
	borderpad=1 #박스형태로 legend 표현
)
plt.show()
```



