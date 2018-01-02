# 1escape Health Club
**Ecommerce & Forum Web Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's classroom bootcamp. It is a **fictional** site built with Python's *Django* framework - no template was used.

## Live Demo

**Follow this link to view deployed version of the web app https://oneescape.herokuapp.com/**

## Built with 
1. Django framework
2. Python
2. HTML
3. CSS
4. Bootstrap
5. Javascript
6. SQLite database

## URL's

urls.py at the project level (fitness) gives the url patterns routes to views.


## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block content %}
{% endblock content %}
```
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:
```
{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}
```

## Apps

#### Home

The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options: "Register" if they have no account or "Log In" if they do. Once Registered/Logged in they can view their own profile that will display their email address they used to register with. The two options will then change to Profile or Log Out. 

#### Products

This App displays the Products that have been added via Django's admin panel.

#### Checkout/Cart

The Cart App stores the quantity and price of all products selected and displays a basket total. The Checkout App then renders a form for a one-off Stripe payment.

#### Contact

The Contact App is used when the 'Contact' link is clicked. The anchor link's href attribute points to the URL 'contact'. From the top level urls.py the 'contact' function is called from the views.py in the Contacts App. This renders the contact.html page which displays the form which has been defined in forms.py within the Contact App. Once the user fills the form in, the 'contact' function is called which checks if the form is valid. If the form is valid, the user is re-directed back to index.html and a Django message appears at the top.

#### Threads

forum.html displays all the subjects that have been created via Django's admin panel, and threads.html displays all the threads. thread.html displays a single thread when clicked. Users must be logged in to create new threads. thread_form.html is the form for creating new threads, and post_form.html for creating new posts inside threads.
 

## Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub.

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.


## Installation

Follow the below instructions to clone this project for c9

1. Create a new workspace
2. Install Django:
    `$ sudo pip3 install django`
3. Create a Django project:
    `$ django-admin startproject fitness .`
4. Create an alias for ‘run’ in .bash_aliases:
```
    alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"
```
5. Create a SECRET_KEY environment variable in .bashrc:
```
    export SECRET_KEY="<secret key goes here>"
```
6. Run the project:
    `$ run`
7. Take the host name from the error and add to Allowed Hosts in settings.py
8. Migrate:
    `$ python3 manage.py migrate`
9. Create a superuser:
    `$ python3 manage.py createsuperuser`
10. Create the apps:
    `$ python3 manage.py startapp accounts`
    `$ python3 manage.py startapp cart`
    `$ python3 manage.py startapp checkout`
    `$ python3 manage.py startapp contact`
    `$ python3 manage.py startapp threads`
    `$ python3 manage.py startapp products`
11. Upload the content from https://github.com/gabrielamuller/stream3_project
12. Install the project dependancies
13. Add to .bashrc:
    ```
    export STRIPE_PUBLISHABLE_KEY=""
    export STRIPE_SECRET_KEY=""
    ```
  
14. Set up an account with Stripe [here](https://stripe.com/gb) & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY.
15. In settings.py change:
```
USE_S3 = os.environ.get("USE_S3", True)
```

To False

16. And change to this:
```
    # DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```
16. In the terminal:
    `$ python3 manage.py make migrations` 
    `$ python3 manage.py migrate` 

16. Log in to the admin panel by going to /admin & log in using the credentials you created for the superuser.
12. You can add products, users, subjects, posts and threads.

## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in and type:

`$ python3 manage.py test <app name>`
