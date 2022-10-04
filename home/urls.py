from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home),
    path('resumedetails/',views.resumedetails),
    path('resumedetails/result',views.result),
]