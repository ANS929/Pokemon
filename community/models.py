from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MathQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=10000)
    content = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'
    
class TCGQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=10000)
    content = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'