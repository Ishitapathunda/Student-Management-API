# 🎓 Student Management System API

A full-stack Student Management System built using **FastAPI**, **React**, **SQLite**, and **JWT Authentication**. The application provides secure user authentication and complete CRUD operations for managing student records.

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Authentication
- Protected API Routes

### 👨‍🎓 Student Management
- Add Student
- View All Students
- Update Student Details
- Delete Student
- RESTful API Design

### 💻 Frontend
- React + Vite
- React Router
- Axios API Integration
- Dashboard
- Login Page
- Register Page
- Students Page
- Navigation Bar
- Logout Functionality

### 🗄️ Database
- SQLite Database
- SQLAlchemy ORM

---

# 🛠️ Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn

## Frontend
- React
- Vite
- React Router DOM
- Axios

---

# 📁 Project Structure

```
Student-Management-System
│
├── backend
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   └── students.db
│
└── frontend
    ├── src
    │   ├── pages
    │   │   ├── Login.jsx
    │   │   ├── Register.jsx
    │   │   ├── Dashboard.jsx
    │   │   └── Students.jsx
    │   │
    │   ├── components
    │   │   └── Navbar.jsx
    │   │
    │   ├── services
    │   │   └── api.js
    │   │
    │   ├── App.jsx
    │   └── main.jsx
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Ishitapathunda/Student-Management-API.git

cd Student-Management-API
```

---

## 2. Backend Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install python-jose
pip install passlib[bcrypt]
pip install python-multipart
```

Run backend

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

Go to frontend folder

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run React

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🔑 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register User |
| POST | `/login` | Login User |

---

## Students

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/students` | Get All Students |
| POST | `/students` | Add Student |
| PUT | `/students/{id}` | Update Student |
| DELETE | `/students/{id}` | Delete Student |

---

# 🔒 Authentication

Protected routes require a JWT token.

Example:

```
Authorization: Bearer <your_access_token>
```

---

# 📸 Screenshots

Add screenshots of:

- Login Page
- Register Page
- Dashboard
- Student Management Page
- Swagger UI

---

# 🌟 Future Improvements

- Search Students
- Pagination
- Profile Management
- Role-Based Access Control
- Docker Deployment
- PostgreSQL Support
- Tailwind CSS UI
- Cloud Deployment (Render/Railway)

---

# 👩‍💻 Author

**Ishita Pathunda**

- GitHub: https://github.com/Ishitapathunda
- LinkedIn: https://www.linkedin.com/in/ishitapathunda/

---

# 📄 License

This project is licensed under the MIT License.
