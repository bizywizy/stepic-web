from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views, authenticate
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *


class IndexView(ListView):
    queryset = Question.objects.new()
    context_object_name = 'questions'
    template_name = 'qa/index.html'
    paginate_by = 10


class PopularView(IndexView):
    queryset = Question.objects.popular()


class AnswersView(FormView):
    form_class = AnswerForm
    template_name = 'qa/detail.html'

    def get_success_url(self):
        return Question.objects.get(id=self.kwargs['pk']).get_absolute_url()

    def get_context_data(self, **kwargs):
        question = Question.objects.get(id=self.kwargs['pk'])
        answers = question.answers.all()
        context = super(AnswersView, self).get_context_data(**kwargs)
        context['question'] = question
        context['answers'] = answers
        return context

    def get_initial(self):
        initial = super(AnswersView, self).get_initial()
        initial['question_id'] = self.kwargs['pk']
        return initial

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.author = self.request.user
        answer.save()
        return redirect(self.get_success_url())


class AskView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = AskForm
    template_name = 'qa/ask.html'

    def form_valid(self, form):
        question = form.save(commit=False)



def ask_page(request):
    if request.method == 'GET':
        form = AskForm()
    elif request.method == 'POST' and request.user.is_authenticated():
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            return redirect(question.get_absolute_url())
    return render(request, 'qa/ask.html', {
        'form': form
    })


def signup_page(request):
    if request.method == 'GET':
        form = SignupForm()
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            views.login(request, user)
            return redirect('index')
    return render(request, 'qa/signup.html', {
        'form': form
    })
