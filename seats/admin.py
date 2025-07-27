from django.contrib import admin
from .models import Student,StudentProfile


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'registration_number', 'department', 'exam_hall', 'seat_number']


# Register your models here.
admin.site.register(Student)
admin.site.register(StudentProfile)