from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('index', views.index),
    path('personal', views.personal),
    path('login_out', views.login_out),
    path('upload_pic', views.upload_pic),
    path('detection',views.detection),
    path('analysis',views.analysis),
    path('get_data',views.get_data),
    path('del_data',views.del_data),
    path('pics',views.pics),
    path('data',views.data),
    path('predict',views.predict),
]
