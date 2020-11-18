
from django.urls import path


from . import views

urlpatterns = [
    path('', views.base_html, name='base_html'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('form/', views.my_first_form, name='my_first_form'),
    path('register/', views.userReg, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('special/', views.special, name='special'),

]