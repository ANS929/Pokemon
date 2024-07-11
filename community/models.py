from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class MathQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=10000)
    #content = models.TextField(null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Math Question'

    def get_absolute_url(self):
        return reverse('account:math_question_details', kwargs={'pk': self.pk})
    
class TCGQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=10000)
    #content = models.TextField(null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - TCG Question'

    def get_absolute_url(self):
        return reverse('account:tcg_question_details', kwargs={'pk': self.pk})
    
class MathComment(models.Model):
    question = models.ForeignKey(MathQuestion, related_name="math_comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    #content = models.TextField(null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.name)

    def get_absolute_url(self):
        return reverse('account:math_question_details', kwargs={'pk': self.question.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TCGComment(models.Model):
    question = models.ForeignKey(TCGQuestion, related_name="tcg_comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    #content = models.TextField(null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.name)

    def get_absolute_url(self):
        return reverse('account:tcg_question_details', kwargs={'pk': self.question.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)