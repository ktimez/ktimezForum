from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AskedQuestions
# Create your views here.



class HomeListView(ListView):
    model = AskedQuestions
    template_name = 'askedquestions_list.html'


class QuestionDetailView(DetailView):
    model = AskedQuestions



class AskCreateView(CreateView):
    pass

