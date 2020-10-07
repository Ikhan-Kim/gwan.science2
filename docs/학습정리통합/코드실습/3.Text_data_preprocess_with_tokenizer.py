# 참고 : https://www.tensorflow.org/tutorials/load_data/text

import tensorflow as tf

import tensorflow_datasets as tfds
import os


# 데이터 다운로드
DIRECTORY_URL = 'https://storage.googleapis.com/download.tensorflow.org/data/illiad/'
FILE_NAMES = ['cowper.txt', 'derby.txt', 'butler.txt']

for name in FILE_NAMES:
  text_dir = tf.keras.utils.get_file(name, origin=DIRECTORY_URL+name)
  
parent_dir = os.path.dirname(text_dir) # '/home/kbuilder/.keras/datasets'


# 데이터 세트에 텍스트로드
# 파일을 반복하여 각 파일을 자체 데이터 세트에로드합니다.
def labeler(example, index):
  return example, tf.cast(index, tf.int64)  

labeled_data_sets = []

for i, file_name in enumerate(FILE_NAMES):
  lines_dataset = tf.data.TextLineDataset(os.path.join(parent_dir, file_name))
  labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
  labeled_data_sets.append(labeled_dataset)


BUFFER_SIZE = 50000
BATCH_SIZE = 64
TAKE_SIZE = 5000

all_labeled_data = labeled_data_sets[0]
for labeled_dataset in labeled_data_sets[1:]:
  all_labeled_data = all_labeled_data.concatenate(labeled_dataset) # concatenate : 배열 결합(참고: https://data-make.tistory.com/132)
  
all_labeled_data = all_labeled_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)



# 텍스트 줄을 숫자로 인코딩
# 기계 학습 모델은 단어가 아닌 숫자로 작동하므로 문자열 값을 숫자 목록으로 변환해야합니다. 이를 위해 고유 한 각 단어를 고유 한 정수에 매핑합니다.

# 어휘 구축
tokenizer = tfds.features.text.Tokenizer()

vocabulary_set = set()
for text_tensor, _ in all_labeled_data:
  some_tokens = tokenizer.tokenize(text_tensor.numpy())
  vocabulary_set.update(some_tokens)

vocab_size = len(vocabulary_set)


# 인코딩 예
encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)

example_text = next(iter(all_labeled_data))[0].numpy()
print(example_text)

encoded_example = encoder.encode(example_text)
print(encoded_example)

# 이제 데이터 세트를 tf.py_function 으로 래핑하고 데이터 세트의 map 메서드에 전달하여 인코더를 실행합니다.
def encode(text_tensor, label):
  encoded_text = encoder.encode(text_tensor.numpy())
  return encoded_text, label

def encode_map_fn(text, label):
  # py_func doesn't set the shape of the returned tensors.
  encoded_text, label = tf.py_function(encode, 
                                       inp=[text, label], 
                                       Tout=(tf.int64, tf.int64))

  # `tf.data.Datasets` work best if all components have a shape set
  #  so set the shapes manually: 
  encoded_text.set_shape([None])
  label.set_shape([])

  return encoded_text, label


all_encoded_data = all_labeled_data.map(encode_map_fn)


# 데이터 세트를 테스트 및 학습 배치로 분할
train_data = all_encoded_data.skip(TAKE_SIZE).shuffle(BUFFER_SIZE)
train_data = train_data.padded_batch(BATCH_SIZE)

test_data = all_encoded_data.take(TAKE_SIZE)
test_data = test_data.padded_batch(BATCH_SIZE)

# 이제 test_data 및 train_data 는 ( example, label ) 쌍의 모음이 아니라 배치 모음입니다. 각 배치는 배열로 표현 된 쌍 ( 많은 예 , 많은 레이블 )입니다.
sample_text, sample_labels = next(iter(test_data))
print(sample_text[0], sample_labels[0])

# 새로운 토큰 인코딩 (패딩에 사용되는 0)을 도입했기 때문에 어휘 크기가 1 씩 증가했습니다.
vocab_size += 1