# Marketplace project
Django project with models:
0. "Register" for user registration
0. "Categories" contains information about market products.
0. "Phones" as a category of products.
***
This project has 2 webpages:
* Registration Form: ("/"),
* Check your email in DB: ("/get/").
***
## Installation (For Linux):
* git clone https://github.com/antl31/Django_register_form
* cd Django_register_form/
* python3 -m venv venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* python3 manage.py migrate
* python3 manage.py runserver
