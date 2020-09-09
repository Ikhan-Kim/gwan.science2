import os
import csv
import numpy as np
import tensorflow as tf

from config import config

import pathlib
import PIL
import PIL.Image

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


# Req. 3-1	이미지 경로 및 캡션 불러오기
def get_path_caption(caption_file_path):
    f = open(caption_file_path, 'r')
    caption_file = csv.reader(f) # 지정된 csvfile의 줄을 이터레이트 하는 판독기(reader) 객체를 반환
    next(caption_file) # 맨 첫줄은 데이터 컬럼명이라 건너뜀

    img_path_list = []  # 모든 이미지 파일명(.jpg)을 담을 리스트(1*n개=31782) [a.jpg, b.jpg, c.jpg, ... ]
    caption_list = []   # 이미지에 대한 모든 캡션을 담을 리스트(이미지 1개당 캡션 5개, n*5개=158910) [[a is a, a is b, ...], [b is b, b is c, ...]]
    for i, line in enumerate(caption_file):
        data = '|'.join(line).split('|') # csv의 구분자인 ,(comma)로 분리된 data를 |로 이어붙인 뒤, |를 기준으로 재분할. ['1000092795.jpg', '0', 'Two young', 'White males are...']
        # 이미지 파일명 저장
        img_path_list.append(data[0])

        # data[1]은 캡션 번호라서 필요 X
        caption = data[2] # 이미지의 캡션([2]~)
        # ,를 포함하던 문장 이어붙이기 ex) 'Two young, White males are...'
        for cap in data[3:]:
            if len(cap) <= 0: 
                break
            else: 
                caption += ',' + cap
        caption_list.append('<start> ' + caption + ' <end> ')

    f.close()
    print("데이터셋 로딩 완료!")

    img_path_list, caption_list = shuffle(img_path_list, caption_list) # 입력된 1개 이상의 배열을 동일한 순서로 섞어준다. 2개 이상의 배열이 입력될 때는 섞을 행의 개수가 같아야 함에 유의한다.

    with open(config.img_description_path, 'w') as f:
        for caption in caption_list:
            f.write("%s\t" % caption) 

    return img_path_list[:config.dataset_size], caption_list[:config.dataset_size]
    


# Req. 3-2	전체 데이터셋을 분리해 저장하기
def dataset_split_save(img_paths, captions):
    train_dataset_path = config.training_dataset_path
    val_dataset_path = config.validation_dataset_path

    # train data와 val data로 분리
    train_img_paths, val_img_paths, train_captions, val_captions = train_test_split(img_paths, captions, test_size=0.2, random_state=0)

    # 분리한 data 저장
    with open(train_dataset_path, 'w') as f:
        for img_path, caption in zip(train_img_paths, train_captions):
            f.write("%s\t%s\n" % (img_path, caption))

    with open(val_dataset_path, 'w') as f:
        for img_path, caption in zip(val_img_paths, val_captions):
            f.write("%s\t%s\n" % (img_path, caption))

    print("데이터셋 분리 및 .txt 저장 완료!")
    return train_img_paths, val_img_paths, train_captions, val_captions
    


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file(dataset_path):
    img_paths = []
    captions = []

    with open(dataset_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split("\t")
            img_paths.append(data[0]) # 이미지 파일명
            captions.append(data[1].rstrip("\n")) # 이미지의 토큰들

    print("%s 데이터셋 로딩 완료!" % dataset_path)
    return img_paths, captions


# Req. 3-4	데이터 샘플링
def sampling_data():
    pass