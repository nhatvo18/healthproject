How to install Django on Mac:

1. Install Homebrew
  https://brew.sh/

2. Install python3
  Run: $ brew install python3

3. Install pipenv:
  Run: $ pip3 install pipenv

4. Install Django (automatically along with a virtual environment):
  Terminal:
    - navigate to an empty folder, ie. ~/Desktop/NewProject
    - run: $ pipenv install django

5. Download this GitHub repo into that folder, ie. ~/Desktop/NewProject

6. In terminal:
  Navigate to your project folder, ie. ~/Desktop/NewProject
  Run: $ pipenv shell
  Navigate to the directory that contains 'manage.py'
  Run: $ python manage.py runserver
  In your browser, go to http://localhost:8000/health/
