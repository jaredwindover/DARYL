# DARYL
Image Classification Hackathon

#Team Members
 - Jared

#Usage:

##First time setup:
    python get-pip.py --user
	[WINDOWS] Add "C:\Python34\Scripts\" to your PATH environement variable
    pip install -r requirements.txt
    #WINDOWS
    pip install virtualenvwrapper-win
    mkvirtualenv daryl
    workon daryl
    #UBUNTU
    pip install virtualenvwrapper
    #Still UBUNTU, Add the following lines to your .bashrc
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

##After each pull:
    pip install -r requirements.txt
    workon daryl

##Before each commit:
    pip freeze > requirements.txt

##To run server:
    cd daryl
    python manage.py runserver

##To view:
Go to http://127.0.0.1:8000 
or
    curl 127.0.0.1:8000
