 Students-Exam-View-
 🪑 Students Exam Seating Arrangement System

A Django-based web application that allows institutions to register students, assign exam halls and seats, and manage exam seating plans efficiently.



 🚀 Features

- 👤 Student Registration with profile photo and department
- 🔐 Secure login/logout system (Django Auth)
- 📋 Admin dashboard for assigning seats and halls
- 🏛 Auto-assignment of exam halls and seat numbers
- 🧾 Profile view with hall and seat info
- 🗂 Staff-only access to seat management
- 🖼 Image upload for student profiles



 📸 Screenshots


static/img/screenshots/login.png
static/img/screenshots/profile.png



 🛠️ Tech Stack

- Backend: Django 5+
- Frontend: HTML5, CSS3, Bootstrap 5, Tailwind (optional)
- Database: SQLite (development), PostgreSQL (production ready)
- Deployment Ready: GitHub / Vercel / PythonAnywhere



 🧪 Running Locally

 🔁 Clone the repository

bash
git clone git@github.com:Janka50/Students-Exam-View-.git
cd Students-Exam-View-


📦 Create & activate virtual environment

bash
python -m venv venv
 On Windows:
venv\Scripts\activate
 On macOS/Linux:
source venv/bin/activate


 📥 Install dependencies

bash
pip install -r requirements.txt


 🔐 Setup the database

bash
python manage.py makemigrations
python manage.py migrate


👤 Create superuser

bash
python manage.py createsuperuser


 🚀 Run the server

bash
python manage.py runserver


Visit: `http://127.0.0.1:8000`



✅ Run Tests

bash
python manage.py test


> Your project currently has 100% passing tests.



 📂 Project Structure
bash

exams/
├── seats/                 # Main Django app
│   ├── models.py          # Student model
│   ├── views.py           # Views for register, login, dashboard, etc.
│   ├── urls.py
│   ├── forms.py
│   ├── templates/seat/    # HTML templates
│   └── tests.py           # Unit tests
├── static/
├── media/
├── db.sqlite3
└── manage.py




 🧠 Future Improvements


- 📲 Student search and filter options
- 🛡 Role-based access control
- 🌐 Full internationalization (i18n)
- ☁️ Deploy to cloud (Render, PythonAnywhere)



 👨‍💻 Author

Abubakar Abdullahi Janka  
[GitHub](https://github.com/Janka50) • [LinkedIn](https://linkedin.com)



 🪪 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
