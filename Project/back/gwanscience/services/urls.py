from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.home, name='home'),
    path('face_reading/', views.face_reading, name='face_reading'),
    path('face_reading/<user_nickname>/<eyebrowInterval>/<eyeSize>/<eyeInterval>/<eyeTail>/<noseLength>/<noseWidth>/<mouthLength>/<mouthThickness>/<mouthTail>/', views.face_reading_get),
    path('name_compability/<str:name_1>/<str:name_2>/', views.name_compability, name='name_compability'),
    path('life_clock/<int:age>/', views.func_life_clock, name='life_clock'),
    # path('split/', views.split, name='split'),
]
# :eyebrowInterval/:eyeSize/:eyeInterval/:eyeTail/:noseLength/:noseWidth/:mouthLength/:mouthThickness/:mouthTail