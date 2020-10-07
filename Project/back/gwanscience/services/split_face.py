# import dlib
# import cv2
# import glob
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# def split_nose(shape, img):
#     X = []
#     Y = []

#     for i in range(27, 36):
#         x, y = shape.part(i).x, shape.part(i).y
#         X.append(x)
#         Y.append(y)

#     t = min(Y)
#     b = max(Y)
#     l = min(X)
#     r = max(X)

#     tmp = img.copy()
#     roi = tmp[t-15:b+15,l-15:r+15]
#     cv2.imwrite("nose123.jpg", roi)

# def split_eye(shape, img):
#     X = []
#     Y = []

#     for i in range(36, 48):
#         x, y = shape.part(i).x, shape.part(i).y
#         X.append(x)
#         Y.append(y)

#     t = min(Y)
#     b = max(Y)
#     l = min(X)
#     r = max(X)

#     tmp = img.copy()
#     roi = tmp[t-15:b+15,l-15:r+15]
#     cv2.imwrite("eye.jpg", roi)

# def split_eyebrow(shape, img):
#     X = []
#     Y = []

#     for i in range(17, 27):
#         x, y = shape.part(i).x, shape.part(i).y
#         X.append(x)
#         Y.append(y)

#     t = min(Y)
#     b = max(Y)
#     l = min(X)
#     r = max(X)

#     tmp = img.copy()
#     roi = tmp[t-15:b+15,l-15:r+15]
#     cv2.imwrite("eyebrow.jpg", roi)

# def split_mouse(shape, img):
#     X = []
#     Y = []

#     for i in range(48, 68):
#         x, y = shape.part(i).x, shape.part(i).y
#         X.append(x)
#         Y.append(y)

#     t = min(Y)
#     b = max(Y)
#     l = min(X)
#     r = max(X)

#     tmp = img.copy()
#     roi = tmp[t-15:b+15,l-15:r+15]
#     cv2.imwrite("mouse.jpg", roi)

# def split_main():
#     print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#     print(glob.glob("*"))
#     imgs = [cv2.imread(file) for file in glob.glob("media/*.jpg")]
#     detector = dlib.get_frontal_face_detector()
#     predictor_path = os.path.join(BASE_DIR, 'shape_predictor_68_face_landmarks.dat')
#     predictor = dlib.shape_predictor(predictor_path)

#     img = imgs.pop()
#     rects = detector(img, 1)
#     for i, rect in enumerate(rects):
#         shape = predictor(img, rect)
#         split_nose(shape, img)
#         split_eye(shape, img)
#         split_eyebrow(shape, img)
#         split_mouse(shape, img)

import dlib
import cv2
import glob
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def split_nose(name, shape, img):
    X = []
    Y = []

    for i in range(27, 36):
        x, y = shape.part(i).x, shape.part(i).y
        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)

    tmp = img.copy()
    roi = tmp[t-10:b+10,l-10:r+10]
    cv2.imwrite(os.path.join(BASE_DIR, "media/split/", name+"_nose.jpg"), roi)

def split_eye(name, shape, img):
    X = []
    Y = []

    for i in range(36, 48):
        x, y = shape.part(i).x, shape.part(i).y
        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)

    tmp = img.copy()
    roi = tmp[t-10:b+10,l-10:r+10]
    cv2.imwrite(os.path.join(BASE_DIR, "media/split/", name+"_eyes.jpg"), roi)

def split_eyebrow(name, shape, img):
    X = []
    Y = []

    for i in range(17, 27):
        x, y = shape.part(i).x, shape.part(i).y
        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)

    tmp = img.copy()
    roi = tmp[t-10:b+10,l-10:r+10]
    cv2.imwrite(os.path.join(BASE_DIR, "media/split/", name+"_glabella.jpg"), roi)

def split_mouse(name, shape, img):
    X = []
    Y = []

    for i in range(48, 68):
        x, y = shape.part(i).x, shape.part(i).y
        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)

    tmp = img.copy()
    roi = tmp[t-10:b+10,l-10:r+10]
    cv2.imwrite(os.path.join(BASE_DIR, "media/split/", name+"_mouth.jpg"), roi)

def split_main(img_name):
    print(img_name)
    imgs = [cv2.imread(file) for file in glob.glob("media/facePhotos/*.png")]
    detector = dlib.get_frontal_face_detector()
    predictor_path = os.path.join(BASE_DIR, 'shape_predictor_68_face_landmarks.dat')
    predictor = dlib.shape_predictor(predictor_path)

    img = imgs.pop()
    rects = detector(img, 1)
    for i, rect in enumerate(rects):
        shape = predictor(img, rect)
        split_nose(img_name, shape, img)
        split_eye(img_name, shape, img)
        split_eyebrow(img_name, shape, img)
        split_mouse(img_name, shape, img)