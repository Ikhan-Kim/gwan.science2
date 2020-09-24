# error시 install cmake
import dlib
# install opencv-python
import cv2
import glob


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
    cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)

def nose():
    X = []
    Y = []

    for i in range(26, 34):
        x, y = shape.part(i).x, shape.part(i).y

        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)
    cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)


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
    cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    return size(t, b, l, r)


def size(t, b, l, r):
    return (b - t) * (r - l)

##이미지 여러장 불러오기
##face 폴더에 얼굴 데이터 추가
imgs = [cv2.imread(file) for file in glob.glob("face/*.jpg")]

## face detector와 landmark predictor 정의
detector = dlib.get_frontal_face_detector()

##shape_predictor_68_face_landmarks.dat파일은 따로 다운받아야 함
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

for k in range(0, len(imgs)):
    img = imgs[k]
    rects = detector(img, 1)
    for i, rect in enumerate(rects):
        shape = predictor(img, rect)
        face_size = face()
        eye_size = eye()

        #얼굴에 있는 각 특징점 찍어 시각화하기
        for j in range(68):
            x, y = shape.part(j).x, shape.part(j).y
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
            string = str(j)
            cv2.putText(img, string, (x - 3, y + 3), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 255), 0, cv2.LINE_AA)

        #눈 상대 면적 구하기
        face_size = face()
        eye_size = eye()
        result = eye_size / face_size * 100

        if result < 0.7:
            print("%3d %.2f%% 작은눈" % (k + 1, result))
        elif result > 1.0:
            print("%3d %.2f%% 큰눈" % (k + 1, result))
        else:
            print("%3d %.2f%% 평균눈" % (k + 1, result))

