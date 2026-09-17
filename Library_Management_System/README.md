# Library Management System

A Django-based CRUD web application for managing library books.

## Features
- Add, view, edit and delete books
- Search books by title, author, ISBN or category
- Book availability status
- Server-side form validation
- REST API for CRUD operations
- Django admin
- SQLite database
- Responsive UI
- Postman-ready API endpoints

## Run in VS Code

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open the development server address shown in the terminal.

## API endpoints
- GET /api/books/
- POST /api/books/
- GET /api/books/<id>/
- PUT/PATCH /api/books/<id>/
- DELETE /api/books/<id>/

## Admin
```bash
python manage.py createsuperuser
```
Then open `/admin/`.
