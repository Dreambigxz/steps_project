from django.shortcuts import render

from .  import forms

from django.http import HttpResponse

# Create your views here.

from .models import Users

from .forms import Newform

def help(request):

    #dict={'insert': 'Help me inserted'}

    return render(request, 'apptwo/help.html')

def users(request):

    fake_users=Users.objects.order_by('first_name')
    #fake_users=x.count()
    cont={'fake': fake_users}

    return render(request, 'apptwo/users.html', context=cont)

def reg(request):

    form= Newform()

    if request.method=='POST':

        form=Newform(request.POST)

        if form.is_valid():
            form.save()

            return help(request)

    return render(request, 'apptwo/register.html', {'forms': form})




