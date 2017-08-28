from .models import AskedQuestions
from django.forms import ModelForm

class AskQ(ModelForm):

    class Meta:
        model = AskedQuestions
        fields = ['title', 'description']
