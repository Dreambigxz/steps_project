from django.urls import path

from .import views

urlpatterns=[

    path('',views.help, name='help'),
    path('users/',views.users, name='users'),
    path('register/',views.reg, name='register'),
]