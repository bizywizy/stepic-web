from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
from .utils import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index_page(request):
    last_questions = Question.objects.new()
    page = paginate(request, last_questions)
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page,
    })


def popular_page(request):
    popular_questions = Question.objects.popular()
    page = paginate(request, popular_questions)
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page
    })


def detail_page(request, pk):
    question = get_object_or_404(Question, pk)
    return render(request, 'qa/detail.html', {
        'question': question
    })