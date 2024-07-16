from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# You Try practice problems
class Practice (models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

class CompletedPractice(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.practice.title}"

# Lesson quizzes
class Quiz(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    correct_answers = models.JSONField(default=dict)
    slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Quizzes"

class CompletedQuiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"
    
    class Meta:
        verbose_name_plural = "Completed quizzes"
    
# Badges
class Badge(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()

    def __str__(self):
        return self.title

class CompletedBadge(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.badge.title}"