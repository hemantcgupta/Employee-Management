# Employee Management API

A Django REST Framework application that allows for CRUD operations on employee records. The application includes user authentication using JWT tokens and stores employee details such as name, email, salary, and phone number.

## Features

- User registration and login with JWT authentication
- CRUD operations for employee records
- Middleware for request processing
- Configurable environment variables using `.env`
- MySQL database support

## Technologies Used

- Django
- Django REST Framework
- MySQL
- Python
- JWT (JSON Web Tokens)
- dotenv for environment variables

## Requirements

- Python 3.11.4 or higher
- Pip 24.0 or higher
- MySQL server

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hemantcgupta/Employee-Management.git
   cd Employee-Management
   ```
2. **Create a `.env` file** in the root directory of your Django project.

3. **Add the following content** to the `.env` file:

    ```env
    # Django settings
    SECRET_KEY=your_secret_key_here
    DEBUG=True  # or False in production

    # Database settings
    DB_NAME=your_db
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_HOST=your_host  
    DB_PORT=your_post  

    # JWT settings
    JWT_SECRET_KEY=your_jwt_secret_key
    JWT_ACCESS_TOKEN_LIFETIME=10  # in minutes

    ```   
4. **Create the database** named as same as `your_db`:

    ```sql
    CREATE DATABASE your_db;
    ```

## Setting Up the Virtual Environment

1. **Create a virtual environment** in the root directory of your project:

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:

    - On **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - On **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

3. **Install dependencies using pip:**
   ```bash
   pip install -r requirements.txt
   ```    

### Database Setup
1. **Make migrations:**
   ```bash
   python manage.py makemigrations
   ```
2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

### Running the Server
Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.   


# API Endpoints Documentation

## Auth Endpoints

### User Signup

- **Endpoint:** `POST /api/signup/`
- **Headers:**
    ```plaintext
    Content-Type: application/json
    ```
- **Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_secure_password"
    }
    ```

### User Login

- **Endpoint:** `POST /api/login/`
- **Headers:**
    ```plaintext
    Content-Type: application/json
    ```
- **Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_secure_password"
    }
    ```
- **Response:**
    ```json
    {
        "refresh": "your_refresh_token",
        "access": "your_access_token"
    }
    ```

# Employee Endpoints

## List Employees

- **Endpoint:** `GET /api/employees/`
- **Headers:**
    ```plaintext
    Authorization: Bearer your_access_token
    ```

## Create Employee

- **Endpoint:** `POST /api/employees/`
- **Headers:**
    ```plaintext
    Content-Type: application/json
    Authorization: Bearer your_access_token
    ```
- **Body:**
    ```json
    {
        "name": "Taylor Swift",
        "email": "taylor@gmail.com",
        "salary": 50000,
        "phone_number": {
            "number": "1234567890"
        }
    }
    ```

## Retrieve Employee

- **Endpoint:** `GET /api/employees/{id}/`
- **Headers:**
    ```plaintext
    Authorization: Bearer your_access_token
    ```

## Update Employee

- **Endpoint:** `PUT /api/employees/{id}/`
- **Headers:**
    ```plaintext
    Content-Type: application/json
    Authorization: Bearer your_access_token
    ```
- **Body:**
    ```json
    {
        "name": "Taylor Swift",
        "email": "taylorswift@gmail.com",
        "salary": 60000,
        "phone_number": {
            "number": "1234567890"
        }
    }
    ```

## Delete Employee

- **Endpoint:** `DELETE /api/employees/{id}/`
- **Headers:**
    ```plaintext
    Authorization: Bearer your_access_token
    ```

