from rest_framework import serializers
from .models import NameCompat
from .algo_name import algo

class NameCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameCompat
        fields = '__all__'