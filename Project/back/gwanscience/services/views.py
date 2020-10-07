from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import NameCompat
from .models import FaceReadingInfo
from .serializers import NameCompatSerializer
from .serializers import FaceReadingInfoSerializer
from .algo_name import algo
from .life_clock import life_clock
from .split_face import split_main

# 분류
from . import eyes_classification as eyes_c
from . import mouth_classification as mouth_c
from . import nose_classification as nose_c
from . import glabella_classification as glabella_c
from . import job

# 사진
import base64
from django.core.files.base import ContentFile
from .models import FaceImage
from PIL import Image
import random
import os
from django.conf import settings
from datetime import datetime
# import six

# 추후삭제
import time
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    pass

@api_view(['POST'])
def face_reading(request):
    # print(request.data)

    present = datetime.now()
    month = str(present.month)
    day = str(present.day)
    hour = str(present.hour)
    minute = str(present.minute)
    second = str(present.second)
    
    user_nickname = request.data.get('nickname')
    user_age = request.data.get('age')
    user_gender = request.data.get('gender') # 1: 남자, 2: 여자
    image_tmp = request.data.get('userPhoto')
    imgstr = image_tmp.split('base64,')[1]
    
    # print(image_tmp)
    
    imgstr = imgstr.replace(" ", "+")
    imgstr += '='*(4-len(imgstr)%4) 
    path = str(os.path.join(settings.MEDIA_ROOT, 'facePhotos/'))
    filename = day +hour +minute +second +"_" +user_age
    
    with open(path + filename +".png", "wb") as f: # sample.jpg 이름으로 저장됩니다.
        f.write(base64.b64decode(imgstr))
        split_main(filename)
    
    # prediction
    eyes_size, eyes_tail, eyes_distance = eyes_c.predict(filename)
    lips_length, lips_thickness, mouth_tail = mouth_c.predict(filename)
    nose_length, nose_width = nose_c.predict(filename)
    glabella_distance = glabella_c.predict(filename)[0]

    eyes = [ eyes_size, eyes_tail, eyes_distance ]
    mouth = [ lips_length, lips_thickness, mouth_tail ]
    nose = [ nose_length, nose_width ]
    glabella = [ glabella_distance ]

    job_data = job.job_classification(eyes, mouth, nose, glabella)

    # face_reading 
    # 변수 초기화
    eyebrowResult = ""
    eyeResult = ""
    noseResult = ""
    mouthResult = ""
    total = ""
    eyebrowInterval = ""

    if glabella_distance == 0:
        eyebrowInterval = "넓은 미간"
        eyebrowResult += "이해심이 넓어 대인관계가 좋음. "
    elif glabella_distance == 1:
        eyebrowInterval = "미간 길이 평균"
        eyebrowResult += "타인을 이해 해주려 하나 고집이 조금 있어 그르치는 경우가 있음. "
    elif glabella_distance == 2:
        eyebrowInterval = "짧은 미간"
        eyebrowResult += "고집이 셈. "
        
    if eyes_size == 0:
        eyeSize = "큰 눈"
        eyeResult += "의지가 있고 강인하며 패기 넘침, 말이 많고 감수성이 강하고, 낙천적이며, 정열이 있으나 관찰력이 약함, 적극적, 사교적이고 유혹에 약함. "
    elif eyes_size == 1:
        eyeSize = "눈 크기 평균"
    elif eyes_size == 2:
        eyeSize = "작은 눈"
        eyeResult += "건실하며 대기만성형 성격이 있으며 주로 자수성가형, 어려움에 당당히 맞설 수 있는 당찬 기질. 자신에 대한 믿음이 강하고 실행력이 뛰어나 많은 사람들, 주변인의 지지와 신임을 얻는 편. 꾀가 많고 치밀함. 왠만한 손해보려 하지 않음. "
        
    if eyes_tail == 0:
        eyeTail = "눈꼬리 내려감"
        eyeResult += "소극적이지만 근성이 있음. 목표를 세워 자신을 잘 다스림. 안정적인것을 선호, 외로움을 많이타고 자존심이 강한사람이 많음, 대인관계 좋음, 말주변이 좋아 임기응변에 능함. "
    elif eyes_tail == 1:
        eyeTail = "눈꼬리 보통"
    elif eyes_tail == 2:
        eyeTail = "눈꼬리 올라감"
        eyeResult += "적극적이면서 명랑하고 정직, 용기가 있으며 자수성가, 자존심이 강해 지는 것을 싫어함, 책임감이 강함, 자신의 영역을 침범받는 것을 싫어하고 자기 방어적인 면을 가지고있음. "
        
    if eyes_distance == 0:
        eyeInterval = "눈 사이가 멂"
        eyeResult += "마음이 넓고 정도가 깊음, 가는 사람 붙잡지 않고 먼 곳을 지향. "
    elif eyes_distance == 1:
        eyeInterval = "눈 사이 거리 평균"
    elif eyes_distance == 2:
        eyeInterval = "눈 사이 짧음"
        eyeResult += "감정이 예민하고 근심걱정을 사서하며 초조하기 쉬움, 먼 곳 보다 바로 앞의 이익을 먼저 생각하여 소견이 좁음. "
        
    if eyeResult == "":
        eyeResult += "티 없는 성격에 주변과의 관계도 원밀하게 좋으며 신임을 얻고 있음. "
        
    if nose_length == 0:
        noseLength = "긴 코"
        noseResult += "사고력과 이해력이 풍부, 도덕성이 뛰어남, 고상한 것을 좋아함. "
    elif nose_length == 1:
        noseLength = "코 길이 보통"
    elif nose_length == 2:
        noseLength = "짧은 코"
        noseResult += "속전속결파, 어디든 잘 적응하며 행동이 싹싹함. "
        
    if nose_width == 0:
        noseWidth = "넓은 콧볼"
        noseResult += "능글맞고, 식욕, 성욕, 물욕이 강함. "
    elif nose_width == 1:
        noseWidth = "콧볼 넓이 보통"
    elif nose_width ==2:
        nose_width = "좁은 콧볼"
        noseResult += "언행이 단순하고 숨김없이 솔직 담백함. "
        
    if noseResult == "":
        noseResult += "코의 크기가 적당하여 조화롭다. 배우자 운이 좋아 행복한 결혼 생활을 할 것. "
        
    if lips_length == 0:
        mouthLength = "긴 입술"
        mouthResult += "포용력이 있고 행동력과 리더쉽이 있음. 부귀와 장수를 나타냄. "
    elif lips_length == 1:
        mouthLength = "입술 길이 보통"
    elif lips_length == 2:
        mouthLength = "짧은 입술"
        mouthResult += "소심하지만 솔직. "
        
    if lips_thickness == 0:
        mouthThickness = "두꺼운 입술"
        mouthResult += "끈기가 있으며, 정욕이 강함. 현실적인 편. "
    elif lips_thickness == 1:
        mouthThickness = "입술 두께 보통"
    elif lips_thickness == 2:
        mouthThickness = "얇은 입술"
        mouthResult += "냉정하며, 금전에 애착이 강함. 이성관계에서는 정신적 교감을 더 중요하게 생각함. "
        
    if mouth_tail == 0:
        mouthTail = "입 꼬리 내려감"
        mouthResult += "자수성가, 경쟁심이 강함. "
    elif mouth_tail == 1:
        mouthTail = "입 꼬리 보통"
    elif mouth_tail == 2:
        mouthTail = "입 꼬리 올라감"
        mouthResult += "외향적, 사교적. "
        
    if mouthResult == "":
        mouthResult = "입이 균형이 잡혀 있으므로 정신적으로나 육체적 또는 감각적으로 모두 안정되어 있으므로 좋은 관상. "   

    # return Response('success')
    result_data ={
        "eyebrowInterval": eyebrowInterval,
        "eyeSize": eyeSize,
        "eyeInterval": eyeInterval,
        "eyeTail": eyeTail,
        "noseLength": noseLength,
        "noseWidth": noseWidth,
        "mouthLength": mouthLength,
        "mouthThickness": mouthThickness,
        "mouthTail": mouthTail,
        "eyebrowResult": eyebrowResult,
        "eyeResult": eyeResult,
        "noseResult": noseResult,
        "mouthResult": mouthResult,
        "job": job_data,

    }
    return Response(result_data)

@api_view(['GET'])
def name_compability(request, name_1, name_2):
    result_data = {"name":[name_1,name_2], "score": [algo(name_1,name_2)[0] ,algo(name_2,name_1)[0]], "cal": [algo(name_1, name_2)[1], algo(name_2, name_1)[1]], "comment": algo(name_1,name_2)[2]}
    return Response(result_data)
    # return JsonResponse(a)

def name_compability_compability(request):
    pass

@api_view(['GET'])
def func_life_clock(request, age):
    time, result, img_url = life_clock(age)
    result_data = {"time":time, "ment":result, "img_url":img_url}
    return Response(result_data)



# @api_view(['GET'])
# def split(request):
#     split_main()
#     return Response('split')


# @api_view(['POST'])
# def face_reading(request):
#     print(request.data)
#     # print(request.data.age)
#     user_nickname = request.data.get('nickname')
#     user_age = request.data.get('age')
#     user_gender = request.data.get('gender') # 1: 남자, 2: 여자
#     print(user_age)

#     image_tmp = list(request.data.keys())
#     print(image_tmp)
#     form, imgstr = image_tmp[0], image_tmp[1]
#     if len(form) > len(imgstr):
#         form, imgstr = imgstr, form
#     print(form, imgstr)
#     imgstr = imgstr.split('base64,')[1]
#     imgstr = imgstr.replace(" ", "+")
#     imgstr += '='*(4-len(imgstr)%4) 

#     path = str(os.path.join(settings.MEDIA_ROOT, 'facePhotos/'))
    
#     with open(path+"sample.jpg", "wb") as f: # sample.png 이름으로 저장됩니다.
#         f.write(base64.b64decode(imgstr))
        
#     # return Response('success')
#     result_data ={
#         "eyebrowShape": "숱이 짙음, 위를 향함",
#         "eyebrowInterval": "미간이 넓음",
#         "eyeSize": "작은 눈",
#         "eyeInterval": "눈 사이가 멂",
#         "eyeTail": "눈 꼬리 올라감",
#         "noseLength": "긴 코",
#         "noseWidth": "긴 인중",
#         "mouthLength": "긴 입술",
#         "mouthThickness": "입술 두꺼움",
#         "mouthTail": "입꼬리 올라감",
#         "eyebrowResult": "이성을 놀이상대로 보지 않음, 통솔력이 좋고 믿음직함, 의리가 좋은 편, 재운과 명예운이 좋음, 너무 두꺼우면 공격적일수 있음. 분명하고 확실한 성격",
#         "eyeResult": "건실하며 대기만성형 성격이 있으며 주로 자수성가형, 어려움에 당당히 맞설 수 있는 당찬 기질, 자신에 대한 믿음이 강하고 실행력이 뛰어나 많은 사람들, 주변인의 지지와 신임을 얻는 편, 적극적이면서 명랑하고 정직, 용기가 있으며 자수성가, 자존심이 강해 지는 것을 싫어함, 책임감이 강함, 자신의 영역을 침범받는 것을 싫어하고 자기 방어적인 면을 가지고있음, 마음이 넓고 정도가 깊음, 가는 사람 붙잡지 않고 멋 곳을 지향",
#         "noseResult": "사고력과 이해력이 풍부, 도덕성이 뛰어나고 규칙적이나 실천력이 부족하고 이론에만 치우치는 경우가 있음, 고상한 것을 좋아함",
#         "mouthResult": "포용력이 있고 행동력과 리더쉽이 있음, 부귀와 장수를 나타냄",
#         "totalResult": "null",

#     }
#     return Response(result_data)