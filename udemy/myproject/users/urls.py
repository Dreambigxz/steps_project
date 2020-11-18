from django.urls import path

from . import views, authviews, myviews
from django.contrib.auth import views as auth_views
from .forms import  UserResetPassword, UserChangePasswordForm


users= 'users'


urlpatterns=[

    path('login-register/', views.log_in, name='login-register'),
    path('logout/', views.log_out, name='logout'),
    path('test/', myviews.SendMail, name='test'),
    # path('test/', myviews.SendMailView.as_view(), name='logout'),




############ Django Auth urls #################


    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset_form.html',
        email_template_name='password/password_reset_email.html',
        form_class=UserResetPassword,
        success_url='sent'
        ), name= 'resetpassword'),

    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_sent.html',
    ), name= 'sent'),
##########################################################################

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/set_password.html',
        form_class= UserChangePasswordForm

    ), name= 'setpassword'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name= 'resetform'),

#########################################################################################################################
]