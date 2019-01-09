How to install Django on Mac:

1. Install Homebrew: https://brew.sh/

2. Install python3: $ brew install python3

3. Install pipenv: $ pip3 install pipenv

4. Install Django (automatically along with a virtual environment):
    - navigate to an empty folder, ie. ~/Desktop/NewProject
    - $ pipenv install django

5. Download this GitHub repo into that folder, ie. ~/Desktop/NewProject

6.
  - Navigate to your project folder, ie. ~/Desktop/NewProject
  - $ pipenv shell
  - Navigate to the directory that contains 'manage.py'
  - $ python manage.py runserver
  - In your browser, go to http://localhost:8000/health/
