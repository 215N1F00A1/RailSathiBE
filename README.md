# 🚉 RailSathiBE

A Django-based backend application for managing train-related services such as **Luggage Service**, **Coach Cleaning**, **Platform Assistance**, and more.

---

## 📚 Features

- ✅ Django Admin Panel for Item Management
- ✅ RESTful API with Django REST Framework
- ✅ Dockerized setup for easy deployment
- ✅ SQLite3 (can easily switch to PostgreSQL)
- ✅ HTML Template view for displaying items

---

## 🔧 Tech Stack

- **Python 3.11**
- **Django 5.x**
- **Django REST Framework**
- **SQLite**
- **Docker & Docker Compose**

---

## 🚀 Getting Started

### 🔁 Clone the Repo

```bash
git clone https://github.com/215N1F00A1/RailSathiBE.git
cd RailSathiBE
# Setup Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
#Install Requirements
pip install -r requirements.txt
#Run Migrations
python manage.py migrate
#Start Development Server
python manage.py runserver
## Admin Panel
Create Superuser
python manage.py createsuperuser
#Django App Output Links (Localhost)
🔹 Home Page (HTML Template View):
Displays the list of items from the database.
👉 http://127.0.0.1:8000/

🔹 Admin Panel (Django Admin):
Requires superuser login to add/update/delete items.
👉 http://127.0.0.1:8000/admin/

🔹 Items API Endpoint (DRF):
Returns JSON for all items (you can test GET, POST, etc.).
👉 http://127.0.0.1:8000/items/

