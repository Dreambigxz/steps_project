from django.db import models

# Create your models here.

class Users(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()



    def __str__(self):
        return (self.first_name + " " + self.last_name)



