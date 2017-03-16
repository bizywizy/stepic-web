from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import PermissionDenied
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

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST' and not request.user.is_authenticated():
            raise PermissionDenied()
        return super(AnswersView, self).dispatch(request, *args, **kwargs)

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


class SignupView(FormView):
    model = User
    form_class = SignupForm
    template_name = 'qa/signup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')

    def form_valid(self, form):
        form.save()
        return redirect('/')
