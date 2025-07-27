from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('my_dashboard/', views.dashboard, name='my_dashboard'),
    path('home/', views.home, name='home'),




  # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='seat/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/auto-assign/', views.auto_assign_seats, name='auto_assign'),

]