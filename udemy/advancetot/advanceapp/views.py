from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy


from .forms import studentDetails, schoolDetails
from django.views.generic import (View,TemplateView, DetailView, ListView,
                                  CreateView, UpdateView, DeleteView)
from .models import School, Students




# Create your views here.


################function base view#####################


def index(request):

    dict= School.objects.all()

    return render(request, 'advanceapp/school.html.', {'school': dict})



def student(request, question_id):



    dict= School.objects.get(pk=question_id)
    return render(request, 'advanceapp/students.html', {'school': dict})


################Class base  view #######################use generic view less code is better

class home(TemplateView):

    template_name = 'advanceapp/home.html'


    def get_context_data(self, **kwargs):
        context= super().get_context_data( *kwargs)

        context['dict']=2+2

        return context

######################################################

class Student_list_view(ListView):


    #define a variable to return all the schools
    #content_object_name= 'schools'

    model = School
    template_name = 'advanceapp/shool_list.html'


class Student_detail_view(DetailView):

    model = School
    template_name = 'advanceapp/school_detail.html'



def schoolForm(request):

    form_1= schoolDetails()
    form_2= studentDetails()

    if request.method =='POST':

        form_1=schoolDetails(data=request.POST)
        form_2=studentDetails(data=request.POST)


        if form_1.is_valid() and form_2.is_valid():

            x=form_1.save()


            y=form_2.save(commit=False)

            y.school=x

            y.save()



            return HttpResponse('Submited')

    else:
        form_1= schoolDetails()
        form_2= studentDetails()

        return render(request, 'advanceapp/register.html', {'form_1': form_1, 'form_2': form_2})





################CRUD#############

######with Djnago class base view ###############

class SchoolCreateView(CreateView):

    model = School
    fields = ('__all__')


class SchoolUpdateView(UpdateView):

    model = School
    fields = ('schoolName', 'principal',)


class SchoolDeleteView(DeleteView):

    model = School

    success_url = reverse_lazy('list')
