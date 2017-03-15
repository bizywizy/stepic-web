from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views, authenticate

from .models import Question
from .utils import paginate
from .forms import *


def index_page(request):
    last_questions = Question.objects.new()
    page = paginate(request, last_questions)
    page.base_url = '/?page='
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page,
    })


def popular_page(request):
    popular_questions = Question.objects.popular()
    page = paginate(request, popular_questions)
    page.base_url = '/popular/?page='
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page
    })


def detail_page(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        form = AnswerForm({'question_id': question.pk})
    elif request.method == 'POST' and request.user.is_authenticated():
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return redirect('detail', pk=question.pk)
    return render(request, 'qa/detail.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form
    })


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

