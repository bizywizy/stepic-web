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


class AnswersView(FormView):  # TODO: forbid POST request if user is anonymous
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


class AskView(LoginRequiredMixin, FormView):
    model = Question
    form_class = AskForm
    template_name = 'qa/ask.html'
    login_url = '/login/'

    def form_valid(self, form):
        question = form.save()
        return redirect(question.get_absolute_url())


class SignupView(FormView):  # TODO: check of user logged in
    model = User
    form_class = SignupForm
    template_name = 'qa/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect('/')
