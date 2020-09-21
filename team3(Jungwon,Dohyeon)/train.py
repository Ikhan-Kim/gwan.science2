from config import config
from data import preprocess 
from utils import utils


# config 저장
utils.save_config("test", config)


# 이미지 경로 및 캡션 불러오기
img_paths, captions = preprocess.get_path_caption(config.caption_file_path)
# 현재 img_paths 에는 파일명만 저장되어있음 ['4939713092.jpg', ...]
img_paths = [config.img_file_path + path for path in img_paths] # 파일명에 경로 추가


# 전체 데이터셋을 분리해 저장하기
train_img_paths, val_img_paths, train_captions, val_captions = preprocess.dataset_split_save(img_paths, captions)


# 저장된 데이터셋 불러오기
img_paths, caption = preprocess.get_data_file(config.training_dataset_path)


# # 데이터 샘플링
# if config.do_sampling:
#     img_paths, caption = preprocess.sampling_data()


# 이미지와 캡션 시각화 하기
utils.visualize_img_caption(img_paths, captions)