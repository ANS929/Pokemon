from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Practice problem
class Practice (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    grade_level = models.CharField(max_length=3, default='')
    slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Submitted practice
class CompletedPractice(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('student', 'practice')

    def __str__(self):
        return f"{self.student.username} - {self.practice.title}"

# Lesson quiz
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=3, default=0)
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

# Submitted quiz
class CompletedQuiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"

    class Meta:
        verbose_name_plural = "Completed quizzes"

# Badge
class Badge(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# Completed badge
class CompletedBadge(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.badge.name}"

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

# Student enrolled in a class
class EnrolledStudent(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"{self.student.username} in {self.course.title}"

# Class to add students to
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title
    
# Child
class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='child')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Children"
    
# Registered child
class RegisteredChild(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_children')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_by_parents')

    def __str__(self):
        return f"{self.parent.username} - {self.student.username}"
    
    class Meta:
        verbose_name_plural = "Registered children"

# Unit (two practices and one quiz)
class Unit(models.Model):
    name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=3, default='')
    slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return f"{self.name} - {self.grade_level} Grade"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)