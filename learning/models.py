from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# You Try practice problems
class Practice (models.Model):
    title = models.CharField(max_length=100)
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
    title = models.CharField(max_length=100)
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
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class CompletedBadge(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.badge.title}"

# Student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Student assigned to a teacher
class RegisteredStudent(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roster')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration')

    def __str__(self):
        return self.student.get_full_name()

# Students enrolled in a class
class EnrolledStudent(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"{self.student.username} in {self.course.title}"

# Classes to add students to
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title