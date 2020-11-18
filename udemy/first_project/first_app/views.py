from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from . models import Topic, AccessRecord, Webpage

from . forms import UserForm, ProfileForm, FormName

from django.urls import resolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
def base_html(request):

    return render(request, 'first_app/base.html')


def index(request):

    webpage= AccessRecord.objects.order_by('date')

    dict={'accr': webpage }

    return render(request, 'first_app/index.html', context=dict)



def home(request):

    return render(request, 'first_app/home.html')


def my_first_form(request):
    form = FormName(request.POST)

    if request.method=='POST':

        form=FormName(request.POST)

        if form.is_valid():

            #do something

            print('Validation successful')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('ext: ' + form.cleaned_data['text'])





    return render(request, 'first_app/form.html', {'form': form})


def userReg(request):

    registered= False

    if request.method == 'POST':

        userForm=UserForm(data=request.POST)
        userProfile=ProfileForm(data=request.POST)


        if userForm.is_valid() and userProfile.is_valid():

            user_name= userForm.cleaned_data['username']
            pass_word= userForm.cleaned_data['password']

            user=userForm.save()
            user.set_password(user.password)
            user.save()

            user = authenticate(username=user_name, password=pass_word)

            if user:
                if user.is_active:
                    login(request, user)

                    return HttpResponseRedirect(reverse('index'))



            profile=userProfile.save(commit=False)

            profile.user=user



            if 'profileImg' in request.FILES:
                profile.profileImg=request.FILES['profileImg']

            profile.save()

            registered=True



        else:
            print(userForm.errors, userProfile.errors)

    else:

        userForm = UserForm()
        userProfile = ProfileForm()


    return render(request, 'first_app/register.html', {
                                                        'userform': userForm,
                                                        'userProfile': userProfile,
                                                        'registered': registered
    })
#
# #
# # ################logout##################
# #
def log_out(request):
     logout(request)
     return HttpResponseRedirect(reverse('base_html'))
# #
# # ################LOGIN ############################




def log_in(request):


    if request.method=='POST':

        phone_number= request.POST.get('phone')
        pass_word= request.POST.get('password')

        user= authenticate(phone=phone_number, password=pass_word)

        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")


        else:
            print('Thise Username:{} And Password: {} tried to login but failed'.format(phone_number, pass_word))
            return HttpResponse("Invalid Detail Supplied")


    else:
      return render(request, 'first_app/login.html', {})




@login_required(login_url='login') #redirect when user is not logged in
def special(request):
    #do something
    return render(request, 'first_app/special.html', {})


