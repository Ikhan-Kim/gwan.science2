from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('api/', views.home, name='home'),
    path('api/face_reading/', views.face_reading, name='face_reading'),
    path('api/name_compability/<str:name_1>/<str:name_2>/', views.name_compability, name='name_compability'),
    path('api/life_clock/<int:age>/', views.func_life_clock, name='life_clock'),
    # path('split/', views.split, name='split'),
]