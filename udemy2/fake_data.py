import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')

import django

django.setup()

##our fke pop

import random

from apptwo.models import  Users

from faker import Faker

fakefiles= Faker()

#topics=['Serch', 'Social', 'Marketplace', 'Games' ]

# def topic():
#
#
#
#     t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
#
#     t.save()
#
#     return t



def popu(n=5):

    for i in range(n):

        #get the topics for entry

        #top= topic()

        #create fake data for the entry
        fake_name= fakefiles.name().split()[1]
        fake_name2= fakefiles.name().split()[1]
        fake_email= fakefiles.email()

        #crate the new webpage entry
        webpage= Users.objects.get_or_create(first_name=fake_name, last_name=fake_name2, email=fake_email)[0]






if __name__== '__main__':

    print('Populating screen')

    popu(20)

    print('Populating complete')
