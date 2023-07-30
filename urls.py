# code
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path("", views.index),
	path("predict/", views.predict),
	path("predict/result", views.result),
]
