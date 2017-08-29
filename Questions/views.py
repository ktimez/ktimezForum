from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AskedQuestions, Replies
from .forms import AskQ
# Create your views here.



class HomeListView(ListView):
    model = AskedQuestions
    template_name = 'askedquestions_list.html'


class QuestionDetailView(DetailView):
    model = AskedQuestions

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        commentss = obj.replies_set.all()
        context['comments'] = commentss
        return context
    
       

class QuestionCreateView(CreateView):
    form_class = AskQ
    template_name = 'addQuestion.html'
    success_url = '/ibibazo/'
    login_url = '/login/'
    

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = request.user
        return super(QuestionCreateView, self).form_valid(form)


