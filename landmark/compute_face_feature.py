import dlib
import cv2
import glob


def face():
    X = []
    Y = []

    for i in range(0, 68):
        x, y = shape.part(i).x, shape.part(i).y

        X.append(x)
        Y.append(y)

    t = min(Y)
    b = max(Y)
    l = min(X)
    r = max(X)
    cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

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


def computeNose():
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


def size(t, b, l, r):
    return (b - t) * (r - l)


# 이미지 여러장 불러오기
# face 폴더에 얼굴 데이터 추가
imgs = [cv2.imread(file) for file in glob.glob("face/*.jpg")]

# face detector와 landmark predictor 정의
detector = dlib.get_frontal_face_detector()

# shape_predictor_68_face_landmarks.dat파일은 따로 다운받아야 함
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

for k in range(0, len(imgs)):
    img = imgs[k]
    rects = detector(img, 1)
    for i, rect in enumerate(rects):
        shape = predictor(img, rect)
        face_size = face()
        eye_size = eye()

        # 얼굴에 있는 각 특징점 찍어 시각화하기
        for j in range(68):
            x, y = shape.part(j).x, shape.part(j).y
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
            string = str(j)
            cv2.putText(img, string, (x - 3, y + 3), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 255), 0, cv2.LINE_AA)

        # 눈 상대 면적 구하기
        face_size = face()
        eye_size = eye()
        tmp = eye_size / face_size * 100
        eye_result = ""
        nose_length = ""
        nose_width = ""
        glabella = ""
        mouse_length = ""
        mouse_thickness = ""
        philtrum = ""
        distance_eyes = ""
        chin = ""

        # 눈 상대 크기 분류
        if tmp < 0.7:
            eye_result = "작음"
        elif tmp > 1.0:
            eye_result = "큼 "
        else:
            eye_result = "평균"

        # 코 길이 비율 구하기
        tmp = (shape.part(33).y - shape.part(27).y) / (shape.part(8).y - shape.part(24).y) * 100
        if tmp < 34:
            nose_length = "짧음"
        elif tmp > 38:
            nose_length = "김 "
        else:
            nose_length = "평균"

        # 코 넓이 비율 구하기
        tmp = (shape.part(35).x - shape.part(31).x) / (shape.part(16).x - shape.part(0).x) * 100
        if tmp < 16:
            nose_width = "좁음"
        elif tmp > 19:
            nose_width = "넓음"
        else:
            nose_width = "평균"

        # 미간 길이 비율 구하기
        tmp = (shape.part(21).x - shape.part(17).x) / (shape.part(22).x - shape.part(21).x) * 100
        if tmp < 150:
            glabella = "김 "
        elif tmp > 240:
            glabella = "좁음"
        else:
            glabella = "평균"

        # 입술 길이
        tmp = (shape.part(54).x - shape.part(48).x) / (shape.part(13).x - shape.part(3).x) * 100
        if tmp < 36:
            mouse_length = "짧음"
        elif tmp > 40:
            mouse_length = "김 "
        else:
            mouse_length = "평균"

        # 입술 두께
        tmp = (shape.part(57).y - shape.part(51).y) / (shape.part(8).y - shape.part(33).y) * 100
        if tmp < 18:
            mouse_thickness = "얇음"
        elif tmp > 29:
            mouse_thickness = "두꺼움"
        else:
            mouse_thickness = "평균"

        # 인중 길이
        tmp = (shape.part(51).y - shape.part(33).y) / (shape.part(8).y - shape.part(57).y) * 100
        if tmp < 40:
            philtrum = "짧음"
        elif tmp > 55:
            philtrum = "김"
        else:
            philtrum = "평균"

        # 눈 사이 거리
        tmp = (shape.part(42).x - shape.part(39).x) / (shape.part(39).x - shape.part(36).x) * 100
        if tmp < 130:
            distance_eyes = "짧음"
        elif tmp > 170:
            distance_eyes = "김 "
        else:
            distance_eyes = "평균"


        print("%3d 눈 크기: %s.\t코 길이: %s.\t코 넓이: %s.\t미간: %s.\t입술 길이: %s.\t입술 두께: %s.\t인중: %s.\t눈 거리: %s."%
              (k + 1, eye_result, nose_length, nose_width, glabella, mouse_length, mouse_thickness, philtrum, distance_eyes))

