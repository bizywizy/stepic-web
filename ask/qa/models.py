from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_query_set().order_by('added_at')

    def popular(self):
        return super(QuestionManager, self).get_query_set().annotate(Count('likes')).order_by('likes__count')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes =  models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
