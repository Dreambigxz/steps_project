from django import forms

from django.core import  validators

from django.contrib.auth.models import User

from .models import  UserProfileModel

#cleaning a specific label
#
# def field_checker(val):
#
#      if val < 8:
#         raise forms.ValidationError('Error here')


class FormName(forms.Form):
    name=forms.CharField(label='First Name')
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter your email again',)
    text= forms.CharField( widget=forms.Textarea)
    bolt= forms.CharField(required=False, widget=forms.HiddenInput,
                          validators=[validators.MaxLengthValidator(0)])



    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        verify = cleaned_data.get("verify_email")

        if email != verify:
            # Only do something if both fields are valid so far.
            # if "help" not in subject:
            raise forms.ValidationError( 'missmatch email')



#now iherit your forms users from the inbuilt djang.contrib User Models

class UserForm(forms.ModelForm):

    username= forms.CharField(label='Nick Name')
    phone= forms.CharField(label='Phone Number')
    password= forms.CharField(label='Password')
    confirm_p= forms.CharField(label='Confirm Password')



    class Meta():
        model=User
        fields=('username', 'email', 'password' )


    #
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm=self.cleaned_data.get('confirm_p')
    #     if len(password) < 1 :
    #         raise forms.ValidationError('too short')
    #
    #     elif '@' not in password:
    #
    #     if password !=  confirm:
    #         raise forms.ValidationError('PASSWORD MISSMATCH')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        verify = cleaned_data.get("confirm_p")

        if password != verify:
            # Only do something if both fields are valid so far.
            # if "help" not in subject:
            raise forms.ValidationError( 'missmatch pass')






        #return super(MyUserCreationForm, self).clean_password1()


#now call your profile and img field model class



class ProfileForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput,
           #                    )
    #profileImg= forms.ImageField()

    class Meta:
        model=UserProfileModel
        fields=  ('portfolio', 'profileImg')





