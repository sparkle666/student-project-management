import profile
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    DEPARTMENT_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Maths', 'Maths'),
        ('Statistics', 'Statistics'),
        ('Physics', 'Physics'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Environmental Science', 'Environmental Science'),
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null = True)

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    supervisor = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='supervisors')
    student = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True,  related_name='students')
    submitted_request = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    request_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    # students = models.ManyToManyField(CustomUser, related_name='projects', through='StudentProject')

class SupervisorRequest(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='project_requests')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requests')
    request_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Request from {self.student.username} for {self.project.title}"