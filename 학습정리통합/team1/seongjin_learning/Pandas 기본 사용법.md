## Pandas 기본 사용법

### Pandas란?

- 데이터를 효과적으로 처리하고, 보여줄 수 있도록 도와주는 라이브러리
- Numpy와 함께 사용되어 다양한 연계적인 기능을 제공
- 인덱스에 따라 데이터를 나열하므로 사전 자료형에 가깝다.
- 시리즈를 기본적인 자료형으로 사용(시리즈 == 인덱스와 값으로 구성됨)



``` python
import pandas as pd

array = pd.Series(['사과', '바나나', '당근'], index=['a', 'b', 'c']])
print(array)
print(array['a'])
```



``` python
import pandas as pd

# Dict 자료형을 Series로 바꾸기
data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근',
}
array = pd.Series(data)
print(array['a'])
```



### 데이터 프레임이란?

- 다수의 시리즈를 모아 처리하기 위한 목적으로 사용함
- 표 형태로 데이터를 손쉽게 출력하고자 할 때 사용함



#### 데이터 프레임 사용하기

``` python
import pandas as pd

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
}
frequency_dict = {
    'Apple': 3,
    'Banana': 5,
	'Carrot': 7,
}
word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
summary = pd.DataFrame([
    'word': word,
    'frequency': frequency
])

print(summary)
```

