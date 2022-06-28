# from django.contrib import admin
# from django.urls import path
# from home import views

# # print("here--------")
# urlpatterns = [
#     path('', views.index, name='home'),
# ]
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), # url without slash
    path('contact', TemplateView.as_view(template_name="index.html"), name="contact"),
]