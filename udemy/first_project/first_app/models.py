from django.contrib.auth.models import User
from django.db import models
#from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

#from .managers import UserManager


class user(AbstractBaseUser, User):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    #objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

















# Create your models here.y


class UserProfileModel(models.Model):

    #inheit a relationaal field from the inbuit user model

    #USERNAME
    #EMAIL
    #PASSWORD
    #FIRSTNAME
    #SURNAME

    user= models.OneToOneField(User, on_delete=models.CASCADE)


    #now add your own fields

    
    portfolio= models.URLField()
    profileImg= models.ImageField(blank=True, upload_to='profile_pic') #direct where you want img uploaded by users to go

    #to handle img from users we have to install library known as pillow


    #now return a string method

    def __str__(self):
        return  self.user.username


class Topic(models.Model):
    topic_name=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, unique=True)
    url= models.URLField(unique=True)

    def __str__(self):
        return self.name



class AccessRecord(models.Model):

    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
