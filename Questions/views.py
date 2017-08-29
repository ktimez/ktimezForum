from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import AskedQuestions, Replies
from .forms import AskQ

from .forms import SignUpForm
from django.contrib.auth import login, authenticate
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
    template_name = 'Questions/addQuestion.html'
    success_url = '/ibibazo/'
    login_url = '/login/'
    

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(QuestionCreateView, self).form_valid(form)






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


