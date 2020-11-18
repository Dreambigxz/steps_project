
from django import forms

from .models import   Users


class Newform(forms.ModelForm):

    email=forms.EmailField()


    # def clean(self):
    #     x= super().clean()
    #
    #     email= x.get('email')
    #
    #     if email :
    #         raise forms.ValidationError('fake')

    class Meta:
        model= Users
        fields= "__all__"


