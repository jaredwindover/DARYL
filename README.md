# DARYL
Image Classification Hackathon

#Team Members
 - Jared

#Usage:

##First time setup:
    pip install -r requirements.txt
    pip install virtualenvwrapper-win
    mkvirtualenv daryl
    workon daryl

##After each pull:
    pip install -r requirements.txt
    workon daryl

##Before each commit:
    pip freeze > requirements.txt

##To run server:
    python manage.py runserver