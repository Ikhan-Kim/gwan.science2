# Tensorflow 강의

### Tensorflow1-1 오리엔테이션

- 기계학습 분류

- 여기서 하는 건 회귀와 분류임.

  - 회귀는 숫자로된 결과를 예측하는 것이고 분류는 카테고리(범주형) 형태의 결과를 예측(음성/양성)

- 머신러닝 알고리즘: 분류와 회귀문제를 풀기 위해서 사용되는 방법(아래는 유명한 알고리즘)
  - Decision Tree
  - Random Forest
  - KNN
  - SVM
  - Neural Network
- Neural Network (=인공신경망=딥러닝)
  - 인공신경망, 딥러닝이라고도 불림.
  - 모두 사람의 뉴런을 모방해서 만든 알고리즘.
- 인공지능 > 기계학습 > 딥러닝
- 딥러닝을 구현하는데 사용되는 라이브러리
  - Tensorflow
  - PyTorch
  - Caffe2
  - theano

### Tensorflow1-3 지도학습의 빅피쳐

- 지도학습하기 위한 과정

  1. 과거의 데이터를 준비함.

     - 독립변수 == 원인 , 종속변수 == 결과

  2. 모델의 구조를 만듬. (변수의 개수에 따라서 구멍의 개수가 달라짐.)

  3. 데이터로 모델을 학습(FIT)함.

  4. 이를 통해서 컴퓨터가 판매량=온도*2 가 된다는 걸 알아냄.

  5. 모델을 이용함. 

  6. 원인이 15도인걸 입력하면 판매량이 30개라는 걸 예상함. 


### Tensorflow1-4 Google Colaboratory - 환경설정

- jupyter notebook - 데이터 분석시 많이 사용
- colab notebook - google drive내에서 jupyter notebook 처럼 사용할 수 있도록 google에서 만든 서비스 
- 사용 방법
  1. 드라이브 - 새로만들기-더보기-연결할 앱 더보기-colaboratory 설치
  2. 새로만들기-더보기-colaboratory를 통해서 파일 생성
  3. 생성된 회색부분을 셀이라고 함. 
     - 실행단축키: ctrl+enter는 해당 셀만 실행시킴. shift+enter는 해당 셀 실행 후 다음 셀 생성.

### Tensorflow1-5 표를 다루는 도구 '판다스'

- 변수 

  - 변수들 사이에 관계가 있을 경우

    - 독립변수: 변수 중 원인이 되는 변수

    - 종속변후: 변수 중 결과가 되는 변수

- 하나의 표안에 독립변수와 종속변수가 같이 있는 데 지도학습은 이걸 구분하는 것에서 시작함.

  - 프로그램을 이용해서 독립변수와 종속 변수를 분리시킴. 

    - 아래는 변수를 분리해서 `독립`과 `종속`이라는 변수에 담음.

  - 이전에 `pandas` import 해줘야함.   `import pandas as pd`


### Tensorflow 1 - 6. 표를 다루는 도구 '판다스' (실습)

- 이번 수업에서 작성한 전체 코드는 가장 밑에 있음.

- csv: `,`를 기준으로 컬럼을 구분한 데이터

- 데이터 준비하기

  1.  `pandas` import 하기 

  2.  csv 파일에서 데이터 읽어오기

     - 파일경로라는 변수에 csv 처장
     - `pandas` 라이브러리에서 `read_csv()` 메소드 사용해서 레모레이드라는 변수에 저장
     - csv 파일을 자동으로 여기에서 사용할 수 있게 변환해 담아줌?

     ```python
     ###########################
     # 라이브러리 사용
     import pandas as pd
      
     ###########################
     # 파일로부터 데이터 읽어오기
     파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
     레모네이드 = pd.read_csv(파일경로)
      
     파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
     보스턴 = pd.read_csv(파일경로)
      
     파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
     아이리스 = pd.read_csv(파일경로)
     ```

  3. 변수에 내가 원하는 모양으로 잘 담겼는지 확인함.

     ```python
     # 데이터의 모양확인
     print(레모네이드.shape)
     print(보스턴.shape)
     print(아이리스.shape)
     ```

     - 아래와 같이 출력됌. (행, 열)을 의미함. 

  4. 독립변수, 종속변수를 분리하기위해서 칼럼이름을 확인해야함. 

     ```python
   # 데이터 칼럼이름 확인
     print(레모네이드.columns)
     print(보스턴.columns)
     print(아이리스.columns)
     ```
  
     - 아래와 같이 출력이 되는데 index라는 이름의 object 형태로 담겨 있음. 

  5. 이후 독립이라는 변수와 종속이라는 변수로 나눠줌.  그리고 잘 나눠졌는지 모양 확인.

     ```python
   # 독립변수와 종속변수 분리
     독립 = 레모네이드[['온도']]
   종속 = 레모네이드[['판매량']]
     print(독립.shape, 종속.shape)
     ```
  
     - 아래와 같이 출력되는데 (행, 열)을 의미하며 당연히 하나의 열이니까 행의 개수==데이터개수
  
  6. 보스턴과 아이리스도 나눠줌. 

     - 보스턴(일단은 medv만 종속으로 해줌.)

       ```python
     독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 
                   'rm', 'age', 'dis', 'rad', 'tax',
                 'ptratio', 'b', 'lstat']]
       종속 = 보스턴[['medv']]
     print(독립.shape, 종속.shape)
       ```
  
       - [[]] 처럼 두번 감싸주는 이유는 해당 컬럼에 대한 내용을 표 형태로 넣기 위해서인듯
  
       - 아래처럼 출력됌. 즉 행이 506개이고 열이 13개인 표가 완성됌.
  
     - 아이리스

       ```python
  독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
       종속 = 아이리스[['품종']]
     print(독립.shape, 종속.shape)
       ```
   
       - 아래처럼 출력됌. 

     - `.head()` : 테이블에서 상위 5개의 데이터를 출력할때 사용하는 method
  
       ```python
    # 각각의 데이터 확인해보기
       print(레모네이드.head())
  print(보스턴.head())
       print(아이리스.head())
     ```
     
     - 아래처럼 출력됌.
     

-  전체 코드

  ```python
  ###########################
  # 라이브러리 사용
  import pandas as pd
   
  ###########################
  # 파일로부터 데이터 읽어오기
  파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
  레모네이드 = pd.read_csv(파일경로)
   
  파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
  보스턴 = pd.read_csv(파일경로)
   
  파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
  아이리스 = pd.read_csv(파일경로)
   
  ###########################
  # 데이터의 모양확인
  print(레모네이드.shape)
  print(보스턴.shape)
  print(아이리스.shape)
   
  ###########################
  # 데이터 칼럼이름 확인
  print(레모네이드.columns)
  print(보스턴.columns)
  print(아이리스.columns)
   
   
  ###########################
  # 독립변수와 종속변수 분리
  독립 = 레모네이드[['온도']]
  종속 = 레모네이드[['판매량']]
  print(독립.shape, 종속.shape)
   
  독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 
              'rm', 'age', 'dis', 'rad', 'tax',
              'ptratio', 'b', 'lstat']]
  종속 = 보스턴[['medv']]
  print(독립.shape, 종속.shape)
   
  독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
  종속 = 아이리스[['품종']]
  print(독립.shape, 종속.shape)
   
   
  ###########################
  # 각각의 데이터 확인해보기
  print(레모네이드.head())
  print(보스턴.head())
  print(아이리스.head())
  ```





### Tensorflow 1 - 7. 레모네이드 판매 예측

- 지도학습 흐름

  1. 과거의 데이터를 준비함.
  
   - tensorflow 1-6 부분임.
  
     ```python
       # 데이터를 준비합니다.
       파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
       레모네이드 = pd.read_csv(파일경로)
       레모네이드.head()   # 데이터 구조를 확인하기 위한 코드
       # 종속변수, 독립변수를 분리
       독립 = 레모네이드[['온도']]
       종속 = 레모네이드[['판매량']]
       print(독립.shape, 종속.shape) # 잘 나눠졌는지 확인.
       ```
  
2. 모델의 구조를 만듬.
  
   - 코드는 아래와 같음. 여기서 중요한건 `shape=[숫자]` 와 `.Dense(숫자)(X)` 에서 `숫자`임.
  
     전자는 독립변수의 개수이고 후자는 종속변수의 개수임. 이걸 위해서 1-6 수업에서 shape을 확인한 것.
  
   - 유전자 알고리즘을 사용하는데 아래는 아주 간단한 뉴런 하나임. 모델을 학습하기 이전의 상태.
  
   - `model.compile(loss='mse')` 은 모델이 학습할 방법을 정해주는 부분
  
     ```python
    # 모델을 만듭니다.
     X = tf.keras.layers.Input(shape=[1])
       Y = tf.keras.layers.Dense(1)(X)
       model = tf.keras.models.Model(X, Y)
       model.compile(loss='mse') # 모델이 학습할 방법을 정해주는 부분
       ```
     
  3. 모델에 데이터를 넣어서 학습시킴.
  
   - 코드는 아래와 같음.  여기서 중요한 건 `epochs=숫자` 로 여기서 숫자가 의미하는 건 전체 데이터를 몇 번 반복해서 학습할 것인지를 정해줌.  여기서는 1000번을 학습하라는 의미
  
   - 이렇게 학습된 모델을 얻을 수 있음.
  
   - 근데 의문은 같은 데이터를 반복해서 학습하는 게 의미가 있는 건가? 컴퓨터가 까먹는 것도 아니고 아니면 이게 주어진 데이터 1000개를 학습하라는 의미인가. 공부하면서 수정해놓을 것.(20.09.10)
  
   - `verbose=0`을 주면 학습하는 과정을 출력하지 않음.  따라서 아래처럼 코드 두번 써준 이유는 10번 하니 loss 가 너무 크게 나옴. 따라서 1000 번 이상으로 많이 해줘야하는데 이 과정을 계속 출력할 수는 없음. 따라서 `verbose=0` 을 주고 학습이 끝났을 때 10번만 더 해봄. 그러면서 loss 값 확인.
  
     ```python
       # 모델을 학습시킵니다. 
     model.fit(독립, 종속, epochs=1000, verbose=0)
       model.fit(독립, 종속, epochs=10)
       ```
  
  4.  모델을 이용함. 즉, 예측해봄.
  
   - `.predict()` 메소드를 이용해서 새로운 값을 학습한 모델에 넣어 예측해봄.
  
     ```python 
       # 모델을 이용합니다. 
     print(model.predict(독립))
       print(model.predict([[15]]))
       ```
  
- 전체 코드

  ```python
  ###########################
  # 라이브러리 사용
  import tensorflow as tf
  import pandas as pd
   
  ###########################
  # 데이터를 준비합니다.
  파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
  레모네이드 = pd.read_csv(파일경로)
  레모네이드.head()
  # 종속변수, 독립변수
  독립 = 레모네이드[['온도']]
  종속 = 레모네이드[['판매량']]
  print(독립.shape, 종속.shape)
   
  ###########################
  # 모델을 만듭니다.
  X = tf.keras.layers.Input(shape=[1])
  Y = tf.keras.layers.Dense(1)(X)
  model = tf.keras.models.Model(X, Y)
  model.compile(loss='mse')
   
  ###########################
  # 모델을 학습시킵니다. 
  model.fit(독립, 종속, epochs=1000, verbose=0)
  model.fit(독립, 종속, epochs=10)
   
  ###########################
  # 모델을 이용합니다. 
  print(model.predict(독립))
  print(model.predict([[15]]))
  ```

  

### Tensorflow 1 - 8. 손실의 의미

- 1-7에서 사용한 코드인`model.fit(독립, 종속, epochs=10)` 에 대한 학습은 아래와 같음.

  - 파란색 부분은 정해준 학습 횟수에서 몇번째인지를 나타냄

  - 주황색 부분은 학습에 걸린 시간

  - 초록색 부분은 학습이 얼마나 진행되었는지를 나타냄. 즉, 각 학습이 끝날때마다 그 시점의 모델이 얼마나 정답에 가깝게 맞추고 있는지를 나타는 지표.

- 학습 흐름

  1. 독립, 종속 변수을 모델에 넣어줌.

  2. 예측을 함. 

  3. 이 모델이 얼마나 좋은지 평가하기 위해서 실제 정답인 종속과 예측 데이터를 비교함.

  4. 예측과 결과의 차이를 제곱함. 그리고 그 값의 평균을 구함. 이 평균 값이 Loss 임.

  5. 예측과 결과의 차이가 적어질 수록 평균값은 0에 수렴하게 됌. 즉 학습이 잘 된 모델임.

  6. 위에서 학습하면서 Loss 가 나오는데 이 Loss 값이 내가 원하는 수준까지 떨어지게 하는게 학습의 목표.

- loss를 떨어뜨리기 위해서 반복해서 학습함.  25까지 떨어짐. 

- 계속 반복해서 학습시키고 0까지 떨어지게 됌. 




### Tensorflow 1 - 10. 보스턴집값예측

- `평균값`을 쓸때 때때로 평균을 제대로 보여주지 못함. 왜냐하면 높은 값이 너무 높을 경우 평균을 끌어 올리기 때문에 이런 경우 이때의 `평균의 대표성`을 무너뜨리는 값들을 `이상치`라고 함. 이런 경우에는 평균 대신 `중앙값`을 사용함. 

- 코드는 아래와 같음.

  ```python
  ###########################
  # 라이브러리 사용
  import tensorflow as tf
  import pandas as pd
   
  ###########################
  # 1.과거의 데이터를 준비합니다.
  파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
  보스턴 = pd.read_csv(파일경로)
  print(보스턴.columns)
  보스턴.head()
   
  # 독립변수, 종속변수 분리 
  독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
              'ptratio', 'b', 'lstat']]
  종속 = 보스턴[['medv']]
  print(독립.shape, 종속.shape)
   
  ###########################
  # 2. 모델의 구조를 만듭니다
  X = tf.keras.layers.Input(shape=[13])
  Y = tf.keras.layers.Dense(1)(X)
  model = tf.keras.models.Model(X, Y)
  model.compile(loss='mse')
   
  ###########################
  # 3.데이터로 모델을 학습(FIT)합니다.
  model.fit(독립, 종속, epochs=1000, verbose=0)
  model.fit(독립, 종속, epochs=10)
   
  ###########################
  # 4. 모델을 이용합니다
  print(model.predict(독립[5:10]))
  # 종속변수 확인
  print(종속[5:10])
   
  ###########################
  # 모델의 수식 확인
  print(model.get_weights())
  ```

- 모델 수식을 확인할 수 있음. 명령문은 `print(model.get_weights())` 임.

  - w,b 값을 수식으로 나타내면 아래와 같음. 두번째 array가 b 값임.

    

- 모델을 학습하는 것의 목표는 w값과 b값을 찾는 것임.

  - 이러한 w를 가중치(weight)라고 함. 
  - 여기서 b를 편향(bias)이라고 부름.

  

- 종속변수가 2개일 경우

  - 종속변수가 두개이므로 최종 수식(모델)이 두개가 필요함.

  

### Tensorflow 1-14. 아이리스 품종 분류 + 1-15 +1-16

- 아이리스 품종 데이터 

  - 독립변수: 꽃잎길이, 꽃잎폭, 꽃받침길이, 꽃받침폭
  - 종속변수: 품종

- 회귀, 분류 알고리즘 

  - 종속변수의 타입에 따라서 어떤 알고리즘을 사용할지가 정해짐.

  - 숫자로 나타내지는 `양적`인 경우 `회귀`(regression) 사용함.

  - T/F 처럼 `범주형`인 경우에는 `분류`(classification)알고리즘을 사용함.

    

- 분류 알고리즘 사용하여 모델 만들기

  1. 과거의 데이터를 준비함.

     - 회귀를 이용할때와 달라진 점

       - `아이리스 = pd.get_dummies(아이리스)` 추가됌.

       - 사진과 같은 수식으로 나타낼 수 있으나 숫자로 나타내야함. 

       - 품종을 모두 칼럼으로 만들어주고 해당 품종인 경우 1로 바꿔줌. 이런 작업을 `원핫인코딩(onehot-encoding)`이라고 함.

       - 원핫인코딩 작업을 `padas`의 `get_dummies()` 메소드를 사용하여 만들 수 있음.

       - 학습하면서 3가지의 모델을 만들어야함. 따라서 모델의 구조를 만들때 출력 Y가 3개임.

         

       ```python
# 라이브러리 사용
       import tensorflow as tf
import pandas as pd
        
###########################
       # 1.과거의 데이터를 준비합니다.
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
       아이리스 = pd.read_csv(파일경로)
       아이리스.head()
        
       # 원핫인코딩
       아이리스 = pd.get_dummies(아이리스)
        
       # 종속변수, 독립변수
       독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
       종속 = 아이리스[['품종_setosa', '품종_versicolor', '품종_virginica']]
       print(독립.shape, 종속.shape)
       ```
     
  2. 모델의 구조를 만듭니다.
  
     - 독립변수의 수가 4개, 종속변수의 수가 3개
  
     - 회귀를 이용할때와 달라진 점
  
       - `activation='softmax'` , `loss='categorical_crossentropy'`이 변경

     - 분류예측 

       - Sigmoid와 Softmax가 있음.

       - softmax는 확률로 예측, 분류함(0~100%).  

         (비가 올 확률은 30%, 동전의 앞뒷면이 나올 확률 50%)

       - 여기서는 softmax를 사용함. (분류 모델의 경우 softmax로 감싸줌. 회귀는 없음.)

       - 예시 

         - 1번째 행은 setosa일 확률이 100%인것.

         - 2번째 행은 setosa일 확률이 70%, virginica일 확률이 30%임. 

         - 회귀모델 같은 경우에는 softmax처럼 감싸주는 게 없음. 이런 softmax같이 출력값을 조절하는 함수를 activation함수라고 함.

         - 문제의 유형에 맞게 loss를 지정해줘야함. 분류와 회귀 다름. 

           - 분류: model.compile(`loss='categorical_crossentropy'`)
  - 회귀: model.compile(`loss='mse'`)
         
       - `metrics='accuracy'`를 추가해주면 정확도를 보여줌. loss는 0에 가까울수록 accuracy는 1에 가까울수록 모델의 예측 정확도가 높음. 
  
     ```python
  # 2. 모델의 구조를 만듭니다
     X = tf.keras.layers.Input(shape=[4])
       Y = tf.keras.layers.Dense(3, activation='softmax')(X)
     model = tf.keras.models.Model(X, Y)
       model.compile(loss='categorical_crossentropy',
                     metrics='accuracy')
     ```
     
    나머지 과정은 동일
  
     ```python
  # 3.데이터로 모델을 학습(FIT)합니다.
     model.fit(독립, 종속, epochs=1000, verbose=0)
     model.fit(독립, 종속, epochs=10)
      
     ###########################
     # 4. 모델을 이용합니다
   # 맨 처음 데이터 5개
     print(model.predict(독립[:5]))
   print(종속[:5])
      
     # 맨 마지막 데이터 5개
     print(model.predict(독립[-5:]))
     print(종속[-5:])
      
     ###########################
     # weights & bias 출력
     print(model.get_weights())
     ```
     
     
  
   







### Numpy

- numpy(Numerical Python)

  - 데이터 셋을 효과적으로 다루기 위한 라이브러리

  - 고성능의 수치 계산을 위해 만들어진 라이브러리

  - 효율적인 데이터분석이 가능하도록 N차원의 배열 객체를 지원 (ndarray) 

    > N차원의 배열 객체가 필요한 이유 : 데이터의 대부분은 숫자 배열로 볼 수 있음.
    >
    > 파이썬 리스트로도 계산 할 수 있지만 numpy는 list에 비해서 빠른 연산을 지원하고 메모리를 효율적으로 사용함. 

- **numpy library**에서 자주 사용하는 함수

  - np.array -> 배열생성
  - np.zeros -> 0이 들어있는 배열 생성
  - np.ones -> 1이 들어있는 배열 생성
  - np.empty -> 초기화가 없는 값으로 배열을 반환
  - np.arrange(n) -> 배열 버전의 range 함수

  ```python 
  # numpy를 활용한 예제
  import numpy as np
  
  # 파이썬에서 리스트 생성시
  list(range(10))
  
  #numpy에서 리스트 생성
  array1 = np.array([1, 2, 3, 4, 5])
  print(array1)
  
  array2 = np.ones((3, 5), dtype=float)
  print(array2)
  
  array3 = np.zeros(10)
  print(array3)
  
  // 출력
  [1 2 3 4 5]
  [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]
  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
  ```

  > 두번째 처럼 요소 하나가 실수이면 나머지도 모두 실수로 출력됌.
  >
  > 세번째 처럼 2차원 배열 만듬.
  >
  > 마지막처럼 모두 실수로 출력되게 할 수 있음.

> 배열 데이터 타입 
>
> python list는 정수, bool, 실수, 문자열 모두 하나의 리스트에 들어갈 수 있지만 numpy는 단일 타입으로만 구성되어야 함. 
>
> 세번째 처럼 하면 arr 배열의 데이터 타입을 int형으로 변경해줌.



- 배열데이터 dtype

  > int32는 32비트 int64는 64비트(64비트가 당연히 더 많은 데이터 저장가능)
  >
  > int64는 i8로 표현되기도 함. 서로 같음.
  >
  > U는 유니 코드

- 배열 만들기

  > 첫번째는 10개의 데이터가 들어간 int 타입의 배열 만들어 달라 근데zeros 이므로 0으로 채움.
  >
  > 두번째는 ones이므로 1로 채우는 데 튜플 형태로 (3,5)로 되어 있는데 배열을 3*5 배열로 만들어 달라.
  >
  > 세번째는 arrange는 파이썬에서 range와 같음. 0부터 20까지 2만큼 뛰면서 배열 하나를 만들어 달라.
  >
  > 네번째는 linspace는 0부터 1까지를 5로 나눠 주고 배열로 만들어 달라는 의미.

- 난수로 채워진 배열 만들기

  > 첫번째 난수로 채워진 배열 만들기 위해서 random 함수 씀. (2,2)는 배열의 형태로 2*2로 만들어 달라.
  >
  > 두번째는 (평균, 표준편차, 배열의형태)로 평균이 0이고 표준편차가 1인 데이터를 2*2 형태로 만들어라.
  >
  > 세번째는 0부터 10까지의 랜덤한 정수를 2*2 형태로 만들어라. 

- 배열 만들기 1

> ndim은 배열의 차원 2차원 배열이니까 2가 출력됌. 
>
> size는 3*4 이니 12로 출력.

- 데이터에 접근하기 

  > 접근하고 변경 및 추가할때 파이썬 list와 같음.

- 데이터 찾고 잘라내기.

  > slicing 이것도 파이썬 list랑 비슷.

- 배열 모양바꾸기

  > reshape을 활요해서 바꿈. 여기서는 2*4 형태로 바꿈.

- 배열 이어 붙이고 나누기

  > ()안에 [x,y]로 써서 리스트 형태로 합침.

- 붙이는 방향 정하기

  > 2*2의 matrix를 만들고 axis가 0을 기준으로 아래로 matrix 두개를 합침.

  > 가로로 붙일때는 axis=1을 사용.

- 배열 나누기

  > split(나눌 배열, [기준인덱스], 방향)
  >
  > 여기서 위쪽 배열은  upper라는 만들어준 변수에 저장되고 아래쪽 배열은 lower에 저장.

>  가로 방향으로 나누기.

- Numpy 연산

  > 루프 사용하여 +5 더하기

> 데이터가 커지만 for문 사용시 느려짐.

- 행렬간 연산

- 브로드 캐스팅

  > shape이 다른 array끼리도 연산이 가능하게 해줌. (자동으로 해주는듯.)

>  이렇게 더해주면 자동으로 1,2,3 해당하는 거 더해줌.

> 이렇게 더해주면 세로로 되있는 것을 옆으로 당겨서 3X3으로 가로로 되어 있는 것을 아래로 당겨서 3X3으로 만들어 준다. 같은 크기로 만듬 그 후 연산. 

- 집계함수

  > 대용량 데이터에 직면했을때 첫단계는 궁금한 데이터에 대해서 요약 통계를 보는 것.
  >
  > 표준편차는 np.std(x)를 통해서 구할 수 있음.

> sum은 축을 통해서 계산할 수도 있음.
>
> 첫번째는 세로방향으로 더해라.
>
> 두번째는 가로방향으로 더해라.

- 마스킹연산

  > 해당 조건에 대해 T/F 반환하거나 T/F에 해당하는 값을 리스트로 반환