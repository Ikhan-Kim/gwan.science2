from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import NameCompat
from .serializers import NameCompatSerializer
from .algo_name import algo
from .life_clock import life_clock
# 추후삭제
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    pass

def face_reading(request):
    pass

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