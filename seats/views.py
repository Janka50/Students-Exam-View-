
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout as django_logout
from .forms import SeatAssignmentForm
from django.contrib.admin.views.decorators import staff_member_required
import random
from django.contrib import messages
from .forms import UserRegistrationForm, StudentProfileForm
from .models import StudentProfile

# Create your views here.

def home(request):
    # You can load students list or stats here.
      students = StudentProfile.objects.all().order_by('exam_hall', 'seat_number')  # sorted nicely
      return render(request, 'seat/home.html', {'students': students})

      return render(request, 'seat/home.html')




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            login(request, user)
            return redirect('profile')
    else:
        user_form = UserRegistrationForm()
        student_form = StudentProfileForm()

    return render(request, 'seat/register.html', {
        'user_form': user_form,
        'student_form': student_form
    })


@login_required
def profile(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        student = None
    return render(request, 'seat/profile.html', {'student': student})


#def logout_view(request):
    #django_logout(request)
    #return redirect('login')


def dashboard(request):
    if request.method == 'POST':
        form = SeatAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_dashboard')
    else:
        form = SeatAssignmentForm()
    return render(request, 'seat/dashboard.html', {'form': form})




@staff_member_required
def auto_assign_seats(request):
    halls = ['A', 'B', 'C', 'D']  # ✅ You can change this list
    seat_counter = {}  # To track the next seat number per hall

    students = Student.objects.all().order_by('id')  # Sort to keep consistent order

    for student in students:
        hall = random.choice(halls)

        # Start seat number at 1 if new hall
        if hall not in seat_counter:
            seat_counter[hall] = 1

        student.exam_hall = hall
        student.seat_number = seat_counter[hall]

        student.save()

        # Increment seat number for that hall
        seat_counter[hall] += 1

    return redirect('home')  # ✅ Or wherever you want to go after


#def home(request):
    # You can load students list or stats here.
     # students = StudentProfile.objects.all().order_by('exam_hall', 'seat_number')  # sorted nicely
      #return render(request, 'seat/home.html', {'students': students})

#      return render(request, 'seat/home.html')

