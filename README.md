#django-project


Endpoints:
1. Register
2. Login
3. Logout
4. Password change
5. Username change
6. Email change

DB:
SQLite

Superuser:
username: dev
password: dev

Postman endpoint collection in file:
postman_api_collection.json

APIs:
Register: http://localhost:8000/auth/users/ POST \
Login: http://127.0.0.1:8000/auth/token/login/ POST \
Logout: http://127.0.0.1:8000/auth/token/logout/ POST \
Auth Status: http://127.0.0.1:8000/auth/authentication_status/ GET \
Change Password: http://localhost:8000/auth/users/set_password/ POST \
Change Username: http://localhost:8000/auth/users/set_username/ POST \
Change Useremail: http://localhost:8000/auth/users/set_username/ POST \

All APIs are accessesable via Django Rest Framework.\

Password complexity validation is handled by "AUTH_PASSWORD_VALIDATORS" of django. \

To active virtual env: cd to project and source cyber_dive_venv/Scripts/activate (Windows) and .\venv\Scripts\activate (Linux) \

To install Requirements: \
pip install django \
pip install django-rest-framework \
pip install djoser \

All migrations have been made. \
To run: python manage.py runserver 0.0.0.0:8000 \
To access Django admin dashboard - Use command {domain}/admin \

Easiest way to trigger the APIs is by importing the JSON file to Postman.\
