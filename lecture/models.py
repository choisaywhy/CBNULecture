from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class College(models.Model):
    college_title = models.CharField(max_length=30)

    def __str__(self):
        return self.college_title

class Department(models.Model):
    college_title = models.ForeignKey(College, on_delete=models.CASCADE, related_name='dept')
    department_title = models.CharField(max_length=30)

    def __str__(self):
        return self.department_title

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    est_year = models.CharField(max_length=5)
    session = models.CharField(max_length=5)
    department_title = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, related_name='dept')
    category = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    prof = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    class_prog = models.CharField(max_length=30)
    class_eval = models.CharField(max_length=30)

class LectureComment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='comment')
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)