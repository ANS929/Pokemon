from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Grade level (1st, 2nd, etc.)
class GradeLevel(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

# Practice problem
class Practice (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(default='', unique=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='practices_in_unit')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='practices')

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
    description = models.TextField()
    correct_answers = models.JSONField(default=dict)
    slug = models.SlugField(default='', unique=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='quizzes')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='quizzes')

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
    perfect_score = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"

    class Meta:
        verbose_name_plural = "Completed quizzes"

    # check if there was improvement from any previous attempts on the same quiz
    def get_improvement(self):
        previous_quizzes = CompletedQuiz.objects.filter(student=self.student, quiz=self.quiz).exclude(id=self.id)
        if previous_quizzes.exists():
            previous_max_score = max(previous_quizzes.values_list('score', flat=True))
            improvement = self.score - previous_max_score
            return improvement
        return 0

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
    slug = models.SlugField(default='', unique=True)
    practices = models.ManyToManyField('Practice', related_name='units')
    quiz = models.OneToOneField('Quiz', on_delete=models.CASCADE, related_name='unit_quiz')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='units')
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Completed unit
class CompletedUnit(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'unit')