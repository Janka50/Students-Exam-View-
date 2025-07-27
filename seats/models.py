from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    exam_hall = models.CharField(max_length=10,blank=True)
    seat_number = models.PositiveIntegerField(blank=True, null=True)
    registration_number = models.CharField(max_length=20, unique=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,null=True )

    def __str__(self):
         return f"{self.user.username} - {self.registration_number}"
    


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    exam_hall = models.CharField(max_length=50, blank=True, null=True)
    seat_number = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

