from .models import AskedQuestions
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AskQ(ModelForm):

    class Meta:
        model = AskedQuestions
        fields = ['title', 'description']



class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='email yawe')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )