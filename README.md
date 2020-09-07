# README

## 개발환경 구축 과정에서 겪은 에러

- ImportError: dll load failed while importing _pywrap_tensorflow_internal

해결 방법: [NVIDIA CUDA 설치](https://developer.nvidia.com/cuda-downloads)



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

