# seats/tests.py
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from seats.models import Student
from seats.forms import UserRegistrationForm, StudentProfileForm, SeatAssignmentForm
from seats import views

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.student = Student.objects.create(
            user=self.user,
            department='CS',
            registration_number='CS2023'
        )

    def test_student_str(self):
        self.assertEqual(str(self.student), f"{self.user.username} - {self.student.registration_number}")

class StudentFormTests(TestCase):
    def test_valid_user_registration_form(self):
        form = UserRegistrationForm(data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_user_registration_form(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())

    def test_valid_student_profile_form(self):
     form = StudentProfileForm(data={
        'department': 'Engineering',
        'exam_hall': 'A',
        'seat_number': 5,
        'registration_number': 'ENG2024'
    })
     self.assertTrue(form.is_valid())

     self.assertTrue(form.is_valid())

    def test_invalid_student_profile_form(self):
        form = StudentProfileForm(data={})
        self.assertFalse(form.is_valid())

class URLTests(TestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, views.profile)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_dashboard_url_resolves(self):
        url = reverse('my_dashboard')
        self.assertEqual(resolve(url).func, views.dashboard)

    def test_auto_assign_url_resolves(self):
        url = reverse('auto_assign')
        self.assertEqual(resolve(url).func, views.auto_assign_seats)

class StudentAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='pass1234'
        )

        self.student = Student.objects.create(
            user=self.user,
            department='CS',
            exam_hall='A',
            seat_number=1,
            registration_number='CSC2023001'
        )

    def test_register_success(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass1234',
            'department': 'Software Engineering',
            'exam_hall': 'B',
            'seat_number': 5,
            'registration_number': 'CSC2023999'
        }, follow=True)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_missing_fields(self):
        response = self.client.post(self.register_url, {
            'username': '',
            'email': '',
            'password': '',
            'department': '',
            'registration_number': ''
        }, follow=True)
        self.assertContains(response, 'This field is required.')

    def test_login_success(self):
        login_success = self.client.login(username='testuser', password='pass1234')
        self.assertTrue(login_success)

    def test_logout_redirects(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.post(self.logout_url, follow=True)
        self.assertRedirects(response, self.login_url)

    def test_profile_authenticated(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seat/profile.html')

    def test_profile_unauthenticated_redirect(self):
        response = self.client.get(self.profile_url)
        self.assertRedirects(response, f"{self.login_url}?next={self.profile_url}")

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client.login(username='admin', password='adminpass')

    def test_dashboard_view_access(self):
        response = self.client.get(reverse('my_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seat/dashboard.html')

    def test_auto_assign_redirect(self):
        Student.objects.create(user=self.user, department='Physics', registration_number='PHY2023')
        response = self.client.get(reverse('auto_assign'))
        self.assertRedirects(response, reverse('home'))
