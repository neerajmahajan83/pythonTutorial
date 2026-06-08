========================================================================
DJANGO PROJECT SETTINGS & DRAFT REPHRASING DOCUMENTATION
========================================================================

PART 1: SETUP A DJANGO PROJECT FROM SCRATCH
------------------------------------------------------------------------
Follow these exact steps in your terminal to set up a clean, isolated 
Django development environment.

Step 1: Set Up and Activate a Virtual Environment
Navigate to your parent directory and run the correct command based on 
your operating system/terminal type.

  * For Linux / macOS / GitHub Codespaces (Bash/Zsh):
    mkdir my_django_project
    cd my_django_project
    python -m venv venv
    source venv/bin/activate

  * For Windows Command Prompt (cmd):
    mkdir my_django_project
    cd my_django_project
    python -m venv venv
    venv\Scripts\activate

  * For Windows PowerShell:
    mkdir my_django_project
    cd my_django_project
    python -m venv venv
    .\venv\Scripts\activate

Step 2: Install Django
Ensure your virtual environment is active (you should see '(venv)' at the 
beginning of your terminal prompt), then run:
  pip install django

Step 3: Create the Django Project
Initialize the project structure. The '.' at the end ensures it installs 
directly in your current directory without nesting an extra folder.
  django-admin startproject config .

Step 4: Run Initial Database Migrations
Apply Django's default migrations for built-in applications (Auth, Sessions):
  python manage.py migrate

Step 5: Start the Development Server
Launch the local web server to verify your installation:
  python manage.py runserver
  -> Open your browser and navigate to: http://127.0.0.1:8000/

Step 6: Initialize a Specific Feature/Application (Optional)
To build components like APIs, blogs, or user portals, spin up a dedicated app:
  python manage.py startapp my_app
  -> Remember to add 'my_app' to the INSTALLED_APPS list in 'config/settings.py'.



# install DB Mysql 
sudo apt update
sudo apt install mysql-server
sudo service mysql start

sudo mysql

CREATE DATABASE django_db;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'django_password';
GRANT ALL PRIVILEGES ON django_db.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

Then update settings.py with:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'django_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


cd /workspaces/pythonTutorial/django
./env/bin/python manage.py migrate



/workspaces/pythonTutorial/django/accounts/views.py



# start env 
. env/bin/activate
or
cd /workspaces/pythonTutorial/django
source env/bin/activate

# start server
python manage.py runserver


## Create a homepage
1. In `django/config/views.py`, add:

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

2. In `django/config/urls.py`, add the view and map the root URL:

```python
from django.contrib import admin
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
```

3. Create the template directory and homepage file:

```bash
cd /workspaces/pythonTutorial/django
mkdir -p templates
cat > templates/home.html <<'EOF'
<!doctype html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome to the Home Page</h1>
  </body>
</html>
EOF
```

4. In `django/config/settings.py`, make sure `TEMPLATES` includes the templates folder:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

5. Run the server and open the home page:

```bash
cd /workspaces/pythonTutorial/django
./env/bin/python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`.
