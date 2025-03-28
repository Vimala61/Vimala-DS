from django.urls import path
from .views import index,  recommend_movie

urlpatterns = [
    path('index/', index, name='index'),
    path('recommend/<str:title>/', recommend_movie, name='recommend_movie'),
]