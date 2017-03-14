from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_queryset().order_by('-added_at')

    def popular(self):
        return super(QuestionManager, self).get_queryset().annotate(models.Count('likes')).order_by('likes__count')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk, ])


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True)
