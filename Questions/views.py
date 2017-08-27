from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AskedQuestions, Replies
# Create your views here.



class HomeListView(ListView):
    model = AskedQuestions
    template_name = 'askedquestions_list.html'


class QuestionDetailView(DetailView):
    model = AskedQuestions

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        post = self.kwargs.get('id')
        obj = self.get_object()
        #print(post)
        commentss = obj.replies_set.all()
        context['comments'] = commentss
        return context
       

class AskCreateView(CreateView):
    pass

