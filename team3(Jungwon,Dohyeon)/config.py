import argparse

# Req. 2-1	Config.py 파일 생성

# 캡션 데이터가 있는 파일 경로 (예시)
# path
parser = argparse.ArgumentParser(description='test')
parser.add_argument('--caption_file_path', type=str, default='./datasets/captions.csv', help="path to caption file")
parser.add_argument('--img_file_path', type=str, default='./datasets/images/', help="path to image file")
parser.add_argument('--img_description_path', type=str, default="./datasets/description.txt", help="image description path")
parser.add_argument('--training_dataset_path', type=str, default="./datasets/training.txt", help="traning dataset path")
parser.add_argument('--validation_dataset_path', type=str, default="./datasets/validation.txt", help="validation dataset path")

# size
parser.add_argument('--dataset_size', type=int, default=6400, help="Set train dataset size")
parser.add_argument('--batch_size', type=int, default=64, help="batch size")

config = parser.parse_args()