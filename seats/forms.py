from django import forms
from django.contrib.auth.models import User
from .models import Student

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['department', 'exam_hall', 'seat_number', 'profile_picture']



class SeatAssignmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'department', 'exam_hall', 'seat_number']



class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'exam_hall', 'seat_number']  # 👈 Exclude fields students shouldn't touch
