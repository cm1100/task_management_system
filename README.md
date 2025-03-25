# Task Management System

A Django-based task management system that allows users to create, assign, and manage tasks. The project uses JWT authentication for secure API access and is containerized using Docker for easy deployment.

---

## Features

- **Task Management**: Create, update, delete, and assign tasks to users.
- **User Authentication**: Secure API endpoints using JWT authentication.
- **Filter Tasks**: Filter tasks by assigned users.
- **Dockerized**: Easily deployable using Docker.

---

## Requirements

- Python 3.12+
- Django 5.1+
- Docker (optional for containerized deployment)
- SQLite (default)

---

## Installation

---

### Dockerized Setup

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:cm1100/task_management_system.git
   cd task_management_system
   ```

1. **Build the Docker Image**:

   ```bash
   sudo docker build -t task_api .
   ```

1. **Run the Docker Container**:

   ```bash
   sudo docker run -p 8000:8000 task_api
   ```

1. **Access the Application**:
   Open your browser and navigate to `http://localhost:8000`.

---

### Local Setup (Without Docker)

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:cm1100/task_management_system.git
   cd task_management_system
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Test Credentials

### Admin User

- **Username**: `admin@example.com`
- **Password**: `admin`

### Test Users

- **Username**: `chaitanya@example.com`
- **Password**: `chaitanya`
- **Username**: `raj@example.com`
- **Password**: `chaitanya`

---

---

## Setting Up VS Code for Running APIs

### Prerequisites

1. Install the **REST Client** extension in VS Code:

   - Go to the Extensions view (`Ctrl+Shift+X`).
   - Search for "REST Client" and install it.

2. Open `documentation/www.http` file and just run with the button present

---
