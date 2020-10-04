from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.home, name='home'),
    path('face_reading/', views.face_reading, name='face_reading'),
    path('face_reading/reading/', views.face_reading_reading, name='face_reading_reading'),
    # path('name_compability/<str:name_1>/<str:name_2>/', views.name_compability, name='name_compability'),
    path('name_compability/', views.name_compability, name='name_compability'),
    path('name_compability/compability/', views.name_compability_compability, name='name_compability_compability'), # 아마 안쓸 듯?
    path('test/<str:name_1>/<str:name_2>/', views.test, name='test'),
]