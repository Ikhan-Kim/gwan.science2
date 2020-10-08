>(코드실습-명세흐름) 실제 플젝 보면서 흐름 파악 및 사용된 모델 학습
>
>이미지 캡셔닝 활용한 플젝 보면서 코드 하나씩 공부하고 정리 중
>
>라이브러리가 실제로 어떻게 쓰이는지 

✍ 학습내용 (코드)



 ### 1. 필요한 라이브러리

#### (1) 머신러닝

- `Numpy` : 행렬이나 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬 라이브러리

  사용예) 배열 생성, 내장함수 이용하여 각종 수치 계산을 위한 기본 패키지

- `Scipy` : 과학 컴퓨팅과 기술 컴퓨팅에 사용되는 수학, 과학, 공학에 대한 자유-오픈 소스 파이썬 라이브러리 => 신호처리, 최적화, 통계 등의 기능을 갖는 패키지를 묶어놓음

- `Scikit-learn` : 기계 학습 라이브러리로 분류, 회귀 분석 및 클러스터링 포험 알고리짐 SVM, 랜덤포레스트, 그래디언트 부스트 등, numpy, scipy 라이브러리와 상호작용하도록 설계됨

#### (2) 딥러닝

- `Tensorflow` : 딥러닝과 기계학습 분야관련 라이브러리

  사용예) 데이터플로우그래프를 통한 풍부한 표현력, 계산 구조와 목표 함수만 정의하면 자동으로 미분 계산 처리 

- `Keras` : 오픈소스 신경망 라이브러리로 딥 신경망과의 빠른 실험을 가능케 하도록 설계됨

#### (3) 시각화

- `Matplotlib` : 파이썬 과학 생태계의 표준 그래프 패키지, 대부분의 그래프를 그릴 수 있음

  사용예) 선그래프, 산점도, 넘파이 배열로 산점도 그리기

- `Tensorboard` : 학습과정 모니터링 툴. 텐스플로우 기반으로 케라스를 구동할 경우 사용 가능함

#### (4) 기타

- `tqdm`  : 함수나 반복문의 진행상황을 progressbar로 나타내주는 라이브러리
- `scikit-image` : 이미지 처리를 위한 라이브러리 (load, save 등)





> **<u>참고하면 좋을 자료</u>**
>
> - 이미지 캡셔닝 전체 흐름 https://www.tensorflow.org/tutorials/text/image_captioning
>
> - 텐서보드 사용 방법 https://blog.naver.com/keeping816/221670552687
>
> - inception 모델에 관한 설명 https://norman3.github.io/papers/docs/google_inception.html
>
> - inception v3 고급 가이드 https://cloud.google.com/tpu/docs/inception-v3-advanced?hl=ko
>
> - 넘파이의 기초통계함수 (평균, 분산, 표준편차, 공분산) https://kongdols-room.tistory.com/70
>
> - 파이썬 pickle 모듈 https://wayhome25.github.io/cs/2017/04/04/cs-04/
>
> - TensorFlow에서 Dataset을 사용하는 방법 https://cyc1am3n.github.io/2018/09/13/how-to-use-dataset-in-tensorflow.html
>
> - TensorFlow Dataset API https://datascienceschool.net/view-notebook/57714103a75c43ed9a7d95f96135f0ad/
>
> - Augmentation https://nittaku.tistory.com/272 
>
>   ​						 https://deepestdocs.readthedocs.io/en/latest/003_image_processing/0030/
>
>   - tf.data API로 성능 향상하기 https://www.tensorflow.org/guide/data_performance?hl=ko
>
> - 모듈 tf.keras.preprocessing.image https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image
>
> - 모듈 tf.image https://www.tensorflow.org/api_docs/python/tf/image?hl=ko-KRChoosing&skip_cache=true
>
> - 신경망 이해하기 (tf.keras.layers.Dense) https://mansculture.com/%EC%8B%A0%EA%B2%BD%EB%A7%9D-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-tf-keras-layers-dens/



### 2. 프로젝트 흐름

#### (1) Data Preprocessing

- Load dataset > Load image data > `CNN` > Extract features of image > Tokenize captions

#### (2) Train & Test Model

- Encode features > Decode features > Calculate loss > Backpropagation > test model



## :deciduous_tree: Directory Architecture

```
├── README.md                 - README.md
├── MD_imgs/                  - README.md에 삽입된 이미지가 저장된 폴더
├── Daily/                    - Daily 팀회의 내용과 각 팀원의 Daily commit md가 저장된 폴더
│
|
├── args/                     - 학습 시 사용된 config 정보가 저장되는 폴더
├── checkpoints/              - 학습된 모델이 저장되는 폴더
│   ├── CNN/                 - Feature를 추출하는 CNN 모델을 저장하는 폴더
│   ├── ckpt/                 - 체크포인트가 저장되는 폴더
|
├── data/                     - 데이터 전처리 관련 폴더
│   ├── __init__.py           - 
│   ├── preprocess.py         - 데이터 전처리
|
├── datasets/                 - 전체 데이터셋
│   ├── images/               - 전체 이미지가 들어있는 폴더
│   ├── textTokenizers/       - 토큰화된 캡션이 저장되는 폴더(.txt)
│   ├── captions.csv          - images 폴더의 이미지 파일명 + 캡션 목록
│   ├── linear_test_x.npy     - 스켈레톤 코드 실행을 위한 샘플 데이터(test)
│   ├── linear_train.npy      - 스켈레톤 코드 실행을 위한 샘플 데이터(train)
│   ├── train.txt             - train 데이터목록(이미지 파일명+캡션)
│   ├── val.txt               - test 데이터목록(이미지 파일명+캡션)
|
├── models/                   - 
│   ├── __init__.py           - 
│   ├── decoder.py            - 텍스트 모델링
│   ├── encoder.py            - 이미지 모델링
│   ├── linear_model.py       - 스켈레톤 코드에 사용된 모델이 정의된 클래스
|
├── utils/                    - 유틸리티 관련 폴더
│   ├── __init__.py           - 
│   ├── utils.py              - 환경 설정과 같은 유틸리티 함수들
│   ├── train_utils.py        - 모델 학습시 필요한 유틸리티 함수들
|
├── config.py                 - 모델 학습시 설정하는 파라미터(argparse)
├── FashionMNIST.py           - Fashion MNIST 데이터를 활용한 머신러닝 예제
├── linear_regression.py      - 스켈레톤 예제
├── predict.py                - 
└── train.py                  - 실제 학습이 이루어지는 main
```



## Sub2

### Req. 1. 이미지 데이터 전처리

#### <u>Req. 1-1. 이미지 파일 로드</u>

> data > preprocess.py

   - 이미지 파일 경로를 입력으로 받아 실제 이미지 데이터를 리턴하는 함수를 구현
   - 이미지 별로 크기가 다른 경우에는 모두 이미지 데이터를 같은 사이즈로 변형

```python
import os
import sys
import csv
import pickle
import gzip
from datetime import datetime
from config import config 📌
import numpy as np 📌
import matplotlib.pyplot as plt
import tensorflow as tf 📌
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# Sub2 Req. 1-1. batch_size 개수만큼 이미지 데이터 로딩
def loading_imgs(img_paths):
    img = tf.io.read_file(img_paths) # 파일을 읽음
    img = tf.image.decode_jpeg(img, channels=3) # 이미지 파일을 디코딩
    img = tf.image.resize(img, (config.image_size, config.image_size)) #이미지 크기 변환
    img = tf.keras.applications.inception_v3.preprocess_input(img)

    return img, img_paths

# ❓ 아래부분은 어떤 기능을 할까유 ? 언제 쓰일까유 ? 
def map_func(img_name, cap):
    img_tensor = np.load(img_name.decode('utf-8') + '.npy')
    return img_tensor, cap
```

📑 img_paths, config.image_size



✍ `tf.io.read_file(이미지_파일경로)` : 파일을 읽음

✍ `tf.image.decode_jpeg(img_읽어온파일, channels=3)` : 파일을 디코딩

✍ `tf.image.resize(img_디코딩한파일, (config.image_size, config.image_size)_resize할크키)` : 이미지 크기 변환

✍ `tf.keras.applications.inception_v3.preprocess_input(img)`

- inception_v3.preprocess_input(img) :  이미지넷 데이터 세트의 평균 RGB 채널을 뺌. 이렇게 하는 이유는 `inception_v3` 모델이 학습 할 때의 전처리 과정이기 때문 => 이 모델의 학습할 때와 같은 전처리를 해주기 위함

  import 할 때 `from tensorflow.keras.applications import inceptio_v3` 이렇게 하면 더욱 간략하게  사용 가능

- `inception_v3` 모델 : 널리 사용되는 이미지 인식 모델로서 ImgeNet 데이터세트에서 78.1% 이상의 정확성을 실현

✍ `np.load(img_name.decode('utf-8') + '.npy')` : np파일을 로드하는데 이미지 이름을 디코드 하고 .npy를 붙임



#### <u>Req. 1-2. 이미지 정규화</u>

> data > preprocess.py

   - 전체 이미지 데이터의 RGB 값의 평균과 분산을 구해 데이터를 정규화 하는 함수를 구현
   - 해당 함수를 이미지 1-1 기능과 합쳐 이미지 파일을 로드할 때 정규화 여부가 전달되고 이에 맞춰 정규화 된 데이터 또는 정규화 되지 않은 데이터를 읽어오도록 함

```python
import os
import sys
import csv
import pickle
import gzip
from datetime import datetime
from config import config
import numpy as np 📌
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Sub2 Req. 1-2. 이미지 정규화
def image_normalization(imgs):
    mean = np.mean(imgs, axis=(0, 1)) # axis: (x, y) 기준으로 평균 계산
    std = np.var(imgs, axis=(0, 1)) # axis: (x, y) 기준으로 분산 계산

    imgs = (imgs-mean)/std

    return imgs
```

📑 imgs

✍ `np.mean(imgs, axis=(0, 1))`

- `numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)`

  mean 함수는 명시된 축을 따라서 산술평균을 계산한다. 이 함수는 배열 요소의 평균값을 반환함. 반환되는 평균값은 기본값으로는 배열 내 모든 요소에 대한 평균값이며 필요할 경우 각 축에 대한 평균값을 구할 수 있다.

  \* 각 입력변수에 대한 설명

  | 변수     | 입력자료형             | 필수입력여부 | 설명                                                         |
  | -------- | ---------------------- | ------------ | ------------------------------------------------------------ |
  | a        | array_like             | 필수         | - 평균값을 구하기 위해 숫자형 자료형을 담고 있는 배열 / - a가 배열이 아닐경우 array로의 컨버전을 시도함 |
  | axis     | None, int, tuple(ints) | 선택         | - 평균값을 구하기 위한 축 혹은 여러개의 축 / - 기본값은 None이며, 이 경우 배열 안에 모든 요소의 평균값을 구한다. / - 정수로 구성된 튜플이 입력될 경우, 여러 축에 대한 평균을 계산한다 |
  | dtype    | dyte-type              | 선택         | - 평균을 계산하는데 사용하는 자료형 의미 / - 정수 배열이 평균을 구하기 위해 입력된 경우, 기본 자료형은 float64 |
  | out      | nd array               | 선택         | - 결과를 배치할 대체 출력 배열을 입력 받음 / - 기본값은 None / - 만약 입력되는 경우, 예상되는 배열의 형상(크기)이 변수에 입력되는 배열의 형상과 동일해야 함 |
  | keepdims | bool                   | 선택         | - 기본값은 아무값도 없는 상태 / True : 결과 계산 후 제거되어지는 축들을 남아있게 함 |



✍ `np.var(imgs, axis=(0, 1))`

- `numpy.var(a, axis=None, dtype=None, out=None, keepdims=<no value>)`

  : 명시된 축을 따라서 분산을 계산. 배열 요소의 분산값을 반환

  반환되는 분산값은 기본값으로는 배열 내 모든 요소에 대한 분산값이며, 필요할 경우 각 축에 대한 분산값을 구할 수 있음

  \* 각 입력변수에 대한 설명

  | 변수     | 입력자료형             | 필수입력여부 | 설명                                                         |
  | -------- | ---------------------- | ------------ | ------------------------------------------------------------ |
  | a        | array_like             | 필수         | - 분산을 구하기 위해 숫자형 자료형을 담고 있는 배열 / - a가 배열이 아닐경우 array로의 컨버전을 시도함 |
  | axis     | None, int, tuple(ints) | 선택         | - 분산을 구하기 위한 축 혹은 여러개의 축 / - 기본값은 None이며, 이 경우 배열 안에 모든 요소의 분산값을 구한다. / - 정수로 구성된 튜플이 입력될 경우, 여러 축에 대한 분산을 계산한다 |
  | dtype    | dyte-type              | 선택         | - 분산을 계산하는데 사용하는 자료형 의미 / - 정수 배열이 평균을 구하기 위해 입력된 경우, 기본 자료형은 float64 |
  | out      | nd array               | 선택         | - 결과를 배치할 대체 출력 배열을 입력 받음 / - 기본값은 None / - 만약 입력되는 경우, 예상되는 배열의 형상(크기)이 변수에 입력되는 배열의 형상과 동일해야 함 |
  | keepdims | bool                   | 선택         | - 기본값은 아무값도 없는 상태 / True : 결과 계산 후 제거되어지는 축들을 남아있게 함 |



### Req. 2. 텍스트 데이터 전처리

#### <u>Req. 2-1. 텍스트 데이터 토큰화</u>

> data > preprocess.py

   - 텍스트 상태인 데이터를 텐서플로우 Tokenizer 를 이용해 각 단어에 해당하는 고유 숫자로 변환(정수 인코딩)

     예) I am hungry => [4, 19, 290]

   - 캡션의 시작과 끝을 표시하기 위해 \<start>, \<end> 토큰 추가

   - 학습에 용이하도록 모든 캡션의 길이를 맞춰주는데 이 때 \<pad> 토큰을 사용

     예) 만약 캡션의 최대 길이를 30으로 정하고 \<pad> 토큰을 2로 정한다면 결과

     I am hungry => \<start> I am hungry \<end> => [0, 4, 19, 290, 1, 2, 2, ..., 2]

     이 때 전체 길이는 30, 2의 개수는 25개

   - 텐서플로우에 구현된 Tokenizer를 찾아보며 구현

``` python
import os
import sys
import csv
import pickle
import gzip
from datetime import datetime
from config import config
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer 📌
from tensorflow.keras.preprocessing import sequence 📌
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Sub2 Req. 2-1 텍스트 데이터 토큰화
def text_tokenizer(tr_captions, val_captions):
    captions = tr_captions + val_captions
    max_length = calc_max_length_caption(captions)

    tokenizer = Tokenizer(num_words=config.top_k, oov_token="<unk>", filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')
    
    ## 단어-색인 및 색인-단어 매핑
    tokenizer.word_index['<pad>'] = 0
    tokenizer.index_word[1] = '<start>'
    tokenizer.word_index['<start>'] = 1
    tokenizer.index_word[2] = '<end>'
    tokenizer.word_index['<end>'] = 2
    tokenizer.fit_on_texts(captions)
	
    ### 모든 시퀀스를 가장 긴 시퀀스와 동일한 길이로 채움
    tr_tokens = tokenizer.texts_to_sequences(tr_captions)
    tr_tokens = sequence.pad_sequences(tr_tokens, maxlen=max_length, padding='post')

    val_tokens = tokenizer.texts_to_sequences(val_captions)
    val_tokens = sequence.pad_sequences(val_tokens, maxlen=max_length, padding='post')

    return tokenizer, tr_tokens, val_tokens

# 캡션 최대길이 정하기
def calc_max_length_caption(captions):
    max = 0
    # 캡션을 토큰화 => 공백분할 => 데이터의 모든 고유단어에 대한 어휘를 얻을 수 있음
    for caption in captions:
        word = caption.split(" ")
        word = [n for n in word if n != "." and n != "," and n != " "]
        length = len(word)
        if max < length:
            max = length

    return max
```

📑 tr_captions, val_captions, calc_max_length_caption, config.top_k

✍ `tokenizer = Tokenizer(num_words=config.top_k, oov_token="<unk>", filters='!"#$%&()*+.,-/:;=?@[\]^_{|}~ ')`

- num_words : 어휘의 크기 제한 (메모리 절약을 위해)
- oov_token : 다른 모든 단어를 unk(알수없음) 토큰으로 바꿈

✍ `tokenizer.fit_on_texts(captions)` : 단어 인덱스를 구축 / 입력에 맞게 내부의 word_index를 만드는 함수 (각 단어마다 고유의 index를 할당)

✍ `tokenizer.texts_to_sequences(tr_captions)` : 문자열을 정수 인덱스의 리스트로 변환 / 문장을 index의 시퀀스로 만듬

✍ `sequence.pad_sequences(val_tokens, maxlen=max_length, padding='post')`

- 문장의 길이를 가장 긴 시퀀스 길이로 맞춰줌
- 모자라는 문장은 padding 값으로 채워짐



#### <u>Req. 2-2. Tokenizer 저장 및 불러오기</u>

> data > preprocess.py

   - 토크나이져를 저장하고 불러 올 수 있는 함수를 구현

     이 때 토크나이져 파일은 파이썬 pickle로 저장

```python
import os
import sys
import csv
import pickle 📌
import gzip
from datetime import datetime
from config import config
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Sub2 Req. 2-2 피클 저장 및 불러오기
def save_load(tokenizer):
    path = ".\\datasets\\textTokenizers\\"
    
    ## tokens를 저장할 폴더가 없으면 생성
    if not os.path.isdir(path):
        os.mkdir(path)

    name = "Tokenizer.pickle"
    name = "".join(i for i in name if i not in "\/:*?<>|")
    name = path + name

    with open(name, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return
```

✍ 파이썬 pickle 모듈

: 일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용하는데, 리스트나 클래스같은 "텍스트가 아닌 자료형"은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.

파이썬에서는 이와 같은 텍스트 이외의 자료형을 파일로 저장하기 위하여 `pickle` 이라는 모듈을 제공한다.

- pickle 모듈을 이용하면 원하는 데이터 자료형의 변경없이 파일로 저장하여 그대로 로드할 수 있다.

  예) `open('text.txt', 'w')` 방식으로 데이터를 입력하면 string 자료형으로 저장됨

  - pickle로 데이터를 저장하거나 불러올 때는 파일을 바이트형식으로 읽거나 써야한다 (wb, rb)

    wb로 데이터를 입력하는 경우는 .bin 확장자를 사용하는게 좋다

  - 입력 `pickle.dump(data, file)`

    ```python
    import pickle
    list = ['a', 'b', 'c']
    with open('list.txt', 'wb') as f:
        pickle.dump(list, f)
    ```

  - 로드 `변수 = pickle.load(file)`

    : 한줄씩 파일을 읽어오고 더이상 로드할 데이터가 없으면 `EOFError` 발생

    ```python
    with open('list.txt', 'rb') as f:
        data = pickle.load(f) # 단 한줄씩 읽어옴
    
    >>> data
    ['a', 'b', 'c']
    ```



### Req. 3. Dataset 생성 함수 구현

#### <u>Req. 3-1. tf.data.Dataset 생성</u>

> data > preprocess.py

   - 이미지 파일 경로와 캡션을 입력으로 받아 **이미지 데이터 및 토큰화된 캡션 쌍**을 리턴하는  함수를 구현
   - 이 때 리턴 값은 텐서플로우 데이터 형식 tf.data.Dataset 을 따르도록 함

```python
import os
import sys
import csv
import pickle
import gzip
from datetime import datetime
from config import config
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 📌
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Sub2 Req. 3-1. tf.data.Dataset 생성
def convert_to_dataset(imgs, tokenizer):

    dataset = tf.data.Dataset.from_tensor_slices((imgs, tokenizer))

    return dataset
```

`tf.data.Dataset.from_tensor_slices((imgs, tokenizer))`

✍ TensorFlow의 `Dataset` : 모델에 데이터를 제대로 공급하기 위해서 입력 파이프라인을 만들어서 GPU로 들어올 데이터를 멈춰있게 하지 않도록 하는 작업을 쉽게 처리해주는 API

✍ `from_tensor_slices((imgs, tokenizer))` : (데이터셋 생성 메서드) 리스트, 넘파이, 텐서플로 자료형에서 데이터셋을 만들 수 있음



#### <u>Req. 3-2. Image Data Augmentation</u>

> data > preprocess.py

   - 이미지 데이터를 받아 매번 랜덤하게 다양한 Augmentation을 적용한 데이터를 리턴하는 함수를 구현
   - 이 때 cf.keras.preprocessing.image 모듈을 참고해 구현
   - 추후 텐서플로우 데이터셋을 생성할 때 Augmentation된 데이터가 캡션과 바인딩 되도록 함

   ```python
import os
import sys
import csv
import pickle
import gzip
from datetime import datetime
from config import config 📌
import numpy as np
import matplotlib.pyplot as plt 📌
import tensorflow as tf 📌
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Sub2 Req. 3-2. Image Data Augmentation
def image_augmentation(dataset):
    augmented_dataset = (
        dataset
        .map(augment, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        .prefetch(tf.data.experimental.AUTOTUNE)
    )

    return augmented_dataset


def augment(image, captions):
    
    image_size = config.image_size
    crop_size = int(image_size * 0.85)

    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_crop(image, size=[crop_size, crop_size, 3])
    image = tf.image.resize(image, (image_size, image_size))
    image = tf.image.random_brightness(image, max_delta=0.5)

    return image, captions

# Image Data Augmentation visualize
def visualize(raw ,original, augmented):
    fig = plt.figure()
    plt.subplot(1,3,1)
    plt.title('Original image')
    plt.imshow(raw)
    plt.subplot(1,3,2)
    plt.title('Normalization image')
    plt.imshow(original)
    plt.subplot(1,3,3)
    plt.title('Augmented image')
    plt.imshow(augmented)
    plt.show()
   ```

📑 config.image_size

✍ Augmentation : 원래 데이터를 부풀려서 성능을 더 좋게 만드는 것

- Augmentation을 하는 중요한 이유

  1) preprocessing과 augmentation 을 하면, 거의 성능이 좋아짐

  2) 원본에 추가되는 개념이라서 성능이 떨어지지 않음

  3) 쉽고 패턴이 정해져있음

- 예

  1) 좌우반전 2) 이미지를 잘라줌 3) 밝기조절 등

- `.map(augment, num_parallel_calls=tf.data.experimental.AUTOTUNE)
          .prefetch(tf.data.experimental.AUTOTUNE)`

  - augment : 데이터 증대

  - `num_parallel_calls=tf.data.experimental.AUTOTUNE`

    - num_parallel_calls : 병렬처리 수준 지정, 병렬 데이터셋을 불러오고 파일을 여는데 기다리는 시간을 단축할 수 있음
    - tf.data.experimental.AUTOTUNE : 어떤 수준의 병렬처리가 tf.data 런타임에 사용되는지에 대해 결정

  - `prefetch(tf.data.experimental.AUTOTUNE)`

    - prefetch = 가져오기 : 전처리와 훈련 스텝의 모델 실행을 오버랩.

       [`tf.data.Dataset.prefetch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset?hl=ko#prefetch)  : 데이터가 소비되는 시간과 데이터가 생성되는 시간 간의 의존성을 줄일 수 있음. 가져올 요소의 수는 하나의 훈련 스텝에서 소비한 배치의 수와 같거나 커야함. 이 값을 수동으로 조정하거나 [`tf.data.experimental.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data/experimental?hl=ko#AUTOTUNE)으로 설정하면 tf.data 런타임이 실행 시에 동적으로 값을 조정하도록 만듦.

      ==> 프리페치 변환은 "프로듀서" 작업과 "컨슈머"의 작업과 오버랩이 가능할 때마다 이점을 제공

  

**✍ tf.keras.preprocessing.image**

: 이미지 데이터에 대한 실시간 데이터 증가를 위한 도구세트



✍ **tf.image 모듈** 

: 이미지 처리 및 디코딩, 인코딩 작업을 위한 다양한 기능을 포함

- `tf.image.convert_image_dtype(image, tf.float32)` : 색 공간 간 변환

  ```python
  tf.image.convert_image_dtype(
      image, dtype, saturate=False, name=None
  )
  ```

- `tf.image.random_flip_left_right(image)` : 이미지를 가로로 무작위로 뒤집음 (왼쪽에서 오른쪽으로)

  ```python
  tf.image.random_flip_left_right(
      image, seed=None
  )
  ```

- `tf.image.random_crop(image, size=[crop_size, crop_size, 3])` : 주어진 크기로 텐서를 무작위로 자름

  ```python
  tf.image.random_crop(
      value, size, seed=None, name=None
  )
  # size = [crop_height, crop_width, 3]
  # RGB의 경우 3??
  ```

- `tf.image.resize(image, (image_size, image_size))` : 이미지 크기 조정

  ```python
  tf.image.resize(
      images, size, method=ResizeMethod.BILINEAR, preserve_aspect_ratio=False,
      antialias=False, name=None
  )
  ```

- `tf.image.random_brightness(image, max_delta=0.5)` : 임의의 요인으로 이미지의 밝기를 조정

  ```python
  tf.image.random_brightness(
      image, max_delta, seed=None
  )
  ```



✍ 사용된 Matplotlib 해석

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





### Req. 4. 이미지 모델(Encoder) 구현

#### <u>Req. 4-1. Pre-trained 모델로 특성 추출</u>

> encoder.py

   - 이미지 데이터의 특성을 뽑아낼 수 있는 함수를 구현

     이 때 GPU를 최대한 사용할 수 있게 batch size를 조정

     => 이 함수의 사용 시점에 따라 이미지 파일의 Augmentation 가능여부나 Decoder에 사용할 수 있는 GPU 의 메모리 공간이 달라지게 되므로 이에 대해 고려해가며 구현

```python
import tensorflow as tf
from config import config


class CNN_Encoder(tf.keras.Model):
    def __init__(self, embedding_dim):
        super(CNN_Encoder, self).__init__()
        self.fc = tf.keras.layers.Dense(embedding_dim)

    def call(self, x):
        x = self.fc(x)
        return x


# Req. 4-1. Pre-trained 모델로 이미지 특성 추출
def create_cnn():
    image_model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')

    new_input = image_model.input
    hidden_layer = image_model.layers[-1].output
    image_feature_extract_model = tf.keras.Model(new_input, hidden_layer)

    # save pre-trained model
    image_feature_extract_model.save(config.cnn_model_path)


def load_cnn():
    model = tf.keras.models.load_model(config.cnn_model_path)
    # model.summary()

    return model


def load_image(image, tokens):
    image = tf.keras.applications.inception_v3.preprocess_input(image)
    return image, tokens
```

📑 tf.keras.Model, embedding_dim, config.cnn_model_path

✍ tf.keras.layers.Dense(embedding_dim) : 규칙적으로 연결된 NN 레이어, 기본 신경망 만들기

```python
tf.keras.layers.Dense(
    units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', 
    bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
    activity_regularizer=None, kernel_constraint=None, bias_constraint=None,
    **kwargs
)
```

✍ tf.keras.applications.InceptionV3(include_top=False, weights='imagenet') : Inception v3 아키텍처를 인스턴스화

- `include_top` : 네트워크의 마지막 계층으로 맨 위에 완전 연결 계층을 포함할지 여부를 나타내는 부울. 기본값은 `True`
- `weights` : `None`(무작위 초기화), `imagenet`(ImageNet에서 사전 훈련) 또는로드 할 가중치 파일의 경로 중 하나 . 기본값은 `imagenet`

✍ tf.keras.Model(new_input, hidden_layer) : `Model` 훈련 및 추론 기능을 사용하여 레이어를 객체로 그룹화

> https://www.tensorflow.org/api_docs/python/tf/keras/Model?hl=ko-KRhttp

✍ tf.keras.models.load_model(config.cnn_model_path) : `model.save()` 로 저장된 모델을 로드



----

## 사용된 Python 코드들

### argparse - 명령행 옵션, 인자와 부속 명령을 위한 파서

```python
import argparse

# 1. argparse.ArgumentParser()를 상속받아 정의
parser = argparse.ArgumentParser(description='Process some integers.')
# 2. add_argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# 3. parser.parse_args()
args = parser.parse_args()
print(args.accumulate(args.integers))
```

위의 파이썬 코드가 `prog.py` 라는 파일에 저장되었다고 가정할 때, 명령행에서 실행되고 유용한 도움말 메시지를 제공할 수 있다:

```bash
$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
```

```bash
$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10
```



### open() - 파일 열기

기본방식

```python
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
```

with문과 같이 쓰기 - with블록을 벗어나는 순간 열린 객체 f가 자동으로 close되어 편리하다.

```python
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
```

"w" : 파일 쓰기, 같은 이름의 파일이 있으면 내용을 지우고 새로 작성

"a" : 기존 파일에 내용 추가

"r" : 파일 읽기



### csv.reader()

지정된 csvfile의 줄을 이터레이트 하는 판독기(reader) 객체를 반환

```python
f = open(caption_file_path, 'r')
caption_file = csv.reader(f)
```



### sklearn - shuffle()

입력된 1개 이상의 배열을 동일한 순서로 섞어준다. 2개 이상의 배열이 입력될 때는 섞을 행의 개수가 같아야 함에 유의한다.

```python
from sklearn.utils import shuffle

img_path_list, caption_list = shuffle(img_path_list, caption_list)
```



### sklearn - train_test_split()

```python
from sklearn.model_selection import train_test_split

train_img_paths, val_img_paths, train_captions, val_captions = 
train_test_split(img_paths, captions, test_size=0.2, random_state=0)
# train_img_paths에는 img_paths에서 (1-0.2)만큼의 데이터가
# val_img_paths에는 나머지(0.2=test_size) 만큼의 데이터가 나뉘어 들어간다
# captions도 동일
```

