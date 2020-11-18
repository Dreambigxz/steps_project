import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

##our fke pop

import random

from .models  import  AccessRecord, Topic, Webpage

from faker import Faker

fakefiles= Faker()

topics=['Serch', 'Social', 'Marketplace', 'Games' ]

def topic():



    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]

    t.save()

    return t



def popu(n=5):

    for i in range(n):

        #get the topics for entry

        top= topic()

        #create fake data for the entry
        fake_url= fakefiles.url()
        fake_date= fakefiles.date()
        fake_name= fakefiles.company()

        #crate the new webpage entry
        webpage= Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]


        accr= AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]



if __name__== '__main__':

    print('Populating screen')

    popu(20)

    print('Populating complete')
