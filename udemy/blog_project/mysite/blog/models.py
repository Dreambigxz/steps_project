from django.db import models
from django.utils import timezone
from datetime import datetime

from django.urls import reverse
sumb= 50 +50
# Create your models here.

class Post(models.Model):

    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tittle= models.CharField(max_length=200)
    text = models.TextField(max_length=600)
    created_date= models.DateField(default=timezone.now)
    balance = models.FloatField(default=0.0)
    published = models.BooleanField(default=False)



    def publish(self):

        self.published= True

        self.save()


    def _save_parents( self, *args, **kwargs):

        if self.published == True:

            self.balance += 50

            super(Post, self)._save_parents(*args, **kwargs)




    def get_absolute_url(self):
        return reverse('detail', kwargs= {'pk': self.pk} )


    def __str__(self):

        return self.tittle



class Comment(models.Model):

    post= models.ForeignKey('Post', on_delete=models.CASCADE)
    author= models.CharField(max_length=200)
    text= models.TextField()
    create_date= models.DateField(default=timezone.now, null=False)
    approved_comment = models.BooleanField(default=False)


    def approve(self):

        self.approved_comment= True

        self.save()

    #def get_absolute_url(self):


    def __str__(self):

        return self.text






