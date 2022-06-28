## Setup
- install pythonn3 and pip3
- ```sudo pip3 install django```
- ```python3 -m django --version```
- ```django-admin startproject mysite``` 
- move to mysite: ```python3 manage.py runserver```
- create module/app: ```python3 manage.py startapp folderName```
- - create urls.py in folderName

- to list all CLI ```python3 manage.py```

## admin
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser``` admin/admin

## template inheritance