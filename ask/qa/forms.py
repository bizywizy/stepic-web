from django.contrib.auth.models import User

from django import forms
from .models import Answer, Question


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Answer
        fields = ['text']

    def save(self, commit=True):
        answer = Answer(**self.cleaned_data)
        answer.question_id = self.initial['question_id']
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user
