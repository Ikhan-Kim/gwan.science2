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

# 사진
import base64
from django.core.files.base import ContentFile
from .models import FaceImage
from PIL import Image
import random
import os
from django.conf import settings

import six

# 추후삭제
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    pass

@api_view(['GET'])
def face_reading(request, username):
    result_data ={
        "username":username,
        "eyebrowShape": "숱이 짙음, 위를 향함",
        "eyebrowInterval": "미간이 넓음",
        "eyeSize": "작은 눈",
        "eyeInterval": "눈 사이가 멂",
        "eyeTail": "눈 꼬리 올라감",
        "noseLength": "긴 코",
        "noseWidth": "긴 인중",
        "mouthLength": "긴 입술",
        "mouthThickness": "입술 두꺼움",
        "mouthTail": "입꼬리 올라감",
        "eyebrowResult": "이성을 놀이상대로 보지 않음, 통솔력이 좋고 믿음직함, 의리가 좋은 편, 재운과 명예운이 좋음, 너무 두꺼우면 공격적일수 있음. 분명하고 확실한 성격",
        "eyeResult": "건실하며 대기만성형 성격이 있으며 주로 자수성가형, 어려움에 당당히 맞설 수 있는 당찬 기질, 자신에 대한 믿음이 강하고 실행력이 뛰어나 많은 사람들, 주변인의 지지와 신임을 얻는 편, 적극적이면서 명랑하고 정직, 용기가 있으며 자수성가, 자존심이 강해 지는 것을 싫어함, 책임감이 강함, 자신의 영역을 침범받는 것을 싫어하고 자기 방어적인 면을 가지고있음, 마음이 넓고 정도가 깊음, 가는 사람 붙잡지 않고 멋 곳을 지향",
        "noseResult": "사고력과 이해력이 풍부, 도덕성이 뛰어나고 규칙적이나 실천력이 부족하고 이론에만 치우치는 경우가 있음, 고상한 것을 좋아함",
        "mouthResult": "포용력이 있고 행동력과 리더쉽이 있음, 부귀와 장수를 나타냄",
        "totalResult": "null",

    }
    return Response(result_data)

def face_reading_reading(request):
    pass

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

# @api_view(['POST'])
# def test(request):
#     faceImage = FaceImage()
#     image_tmp = list(request.data.keys())
#     print(image_tmp)
#     print(image_tmp[0])
#     format, imgstr = image_tmp[0], image_tmp[1]
#     imgstr = imgstr.split('base64,')[1]
#     imgstr += '='*(4-len(imgstr)%4) 
#     # imgstr = imgstr.strip()

#     ext = format.split('/')[-1]
#     faceImage.user_img = ContentFile(base64.b64decode(imgstr), name='face.' + ext)
#     faceImage.save()
#     return Response('success')

@api_view(['POST'])
def test(request):
    # faceImage = FaceImage()
    print(request.data)
    image_tmp = list(request.data.keys())
    format, imgstr = image_tmp[0], image_tmp[1]
    print(format)
    print(imgstr)
    imgstr = imgstr.split('base64,')[1]
    imgstr += '='*(4-len(imgstr)%4) 
    # print(imgstr)
    number = random.randrange(1,100)
    if isinstance(imgstr, six.string_types):
        print('yes')
    else:
        print('no')

    path = str(os.path.join(settings.MEDIA_ROOT, 'testImg/'))
    filename = 'image'+str(number)+'.png'

    image = open(path+filename,'wb')
    image.write(base64.b64decode(imgstr))
    image.close()
    
    return Response('success')

@api_view(['GET'])
def split(request):
    split_main()
    return Response('split')





    # print(base64.b64encode(request.data))


    # serializer = FaceReadingInfoSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)