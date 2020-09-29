from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import NameCompat
from .serializers import NameCompatSerializer
from .algo_name import algo

# Create your views here.
def home(request):
    pass

def face_reading(request):
    pass

def face_reading_reading(request):
    pass

@api_view(['POST'])
def name_compability(request):
    serializer = NameCompatSerializer(data=request.data)
    name1 = request.data.get('name1')
    name2 = request.data.get('name2')
    
    if serializer.is_valid():
        serializer.save(jumsu1=algo(name1, name2), jumsu2=algo(name2,name1))
        return Response(serializer.data)

def name_compability_compability(request):
    pass