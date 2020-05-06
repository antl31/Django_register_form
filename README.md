# Marketplace project
Django project with models:
1."Register" for user registration
2."Categories" contains information about market products.
3."Phones" as a category of products.
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
