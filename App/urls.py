from django.urls import path, include
from django.contrib import admin
from App import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('register/', views.register_user, name = 'registration'),
	path('upload/', views.upload, name = 'upload'),
	path('tstudent/', views.tstudent, name = 'tstudent'),
	path('upload/list-files/', views.list_files, name = 'listfiles'),
]