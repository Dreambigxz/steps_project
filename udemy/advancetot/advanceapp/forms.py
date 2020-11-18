
from django.forms import ModelForm

from .models import Students, School

class schoolDetails(ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class studentDetails(ModelForm):

    class Meta:
        model = Students
        exclude = ('school',)


