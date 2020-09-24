import dlib
import cv2
import glob

def face():
    X = []
    Y = []

    for i in range(0, 67):
        x, y = shape.part(i).x, shape.part(i).y

        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)
    # cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)

def eye():
    X = []
    Y = []

    for i in range(36, 41):
        x, y = shape.part(i).x, shape.part(i).y

        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)
    # cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)

def nose():
    X = []
    Y = []

    for i in range(27, 35):
        x, y = shape.part(i).x, shape.part(i).y

        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)
    # cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)

def noseROI():
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

    roi = tmp[t-15:b+15,l-15:r+15]
    cv2.imshow("nose", roi)

def eyeROI():
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

    roi = tmp[t-15:b+15,l-15:r+15]
    cv2.imshow("eye", roi)

def eyebrowROI():
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
    roi = tmp[t-15:b+15,l-15:r+15]
    cv2.imshow("eyebrow", roi)

def mouseROI():
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

    roi = tmp[t-15:b+15,l-15:r+15]
    cv2.imshow("mouse", roi)

def size(t, b, l, r):
    return (b - t) * (r - l)

imgs = [cv2.imread(file) for file in glob.glob("face/*.jpg")]

## face detector와 landmark predictor 정의
detector = dlib.get_frontal_face_detector()

##shape_predictor_68_face_landmarks.dat파일은 따로 다운받아야 함
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

##처리할 이미지 번호 지정
img_idx = 340

for k in range(img_idx-1, img_idx):
    img = imgs[k]
    img = cv2.resize(img, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    rects = detector(img, 1)
    for i, rect in enumerate(rects):
        shape = predictor(img, rect)
        face_size = face()
        eye_size = eye()

        # 얼굴에 있는 각 특징점 찍어 시각화하기
        # for j in range(68):
        #     x, y = shape.part(j).x, shape.part(j).y
        #     cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
        #     string = str(j)
        #     cv2.putText(img, string, (x - 3, y + 3), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 255), 0, cv2.LINE_AA)

        cv2.imshow('frame', img)
        noseROI()
        eyeROI()
        eyebrowROI()
        mouseROI()
        cv2.waitKey(0)
        cv2.destroyWindow('frame')
