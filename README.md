# DARYL
Image Classification Hackathon

#Team Members
 - Jared

#Usage:

##First time setup:
    python get-pip.py --user
	[WINDOWS] Add "C:\Python34\Scripts\" to your PATH environement variable
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