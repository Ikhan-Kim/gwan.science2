from rest_framework import serializers
from .models import NameCompat
from .models import FaceReadingInfo
from .algo_name import algo

class NameCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameCompat
        fields = '__all__'

class FaceReadingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceReadingInfo
        fields = 'user_img'