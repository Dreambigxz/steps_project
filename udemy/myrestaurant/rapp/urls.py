from django.urls import path

from . import views

urlpatterns=[

    path('', views.homeTemplate.as_view(), name='home')


]