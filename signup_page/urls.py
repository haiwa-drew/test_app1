from django.urls import path
from . import views



urlpatterns = [
    path('' , views.index , name='signup'),
    path('homepage', views.homepage, name= 'homepage')
]