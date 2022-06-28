# from django.contrib import admin
# from django.urls import path
# from home import views

# # print("here--------")
# urlpatterns = [
#     path('', views.index, name='home'),
# ]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]