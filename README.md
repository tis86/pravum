# HOW TO START

## CLONE REPO AND MAKE SOME PREPARATION FOR DEVELOPMENT
1. sudo apt install python3.8-venv venv
2. cd <working_dir>
3. python3 -m venv ./env
4. source env/bin/activate
5. git clone https://github.com/tis86/pravum.git
6. pip install requirements.txt
7. ./manage.py makemigrations && ./manage.py migrate

## THERE THRE TYPES OF STARTING

### THIRST USING DEFAULT FROM DJANGO
1. In project dir you have to run this command(but there will be some errors
which you need to fix)

> ./manage.py runserver

### SECOND USING DOCKER

1. For windows you have to install Docker Desktop
2. For linux you should install these packages

> sudo apt install docker.io docker docker-engine

3. After that you can build your docker image using this command

> docker build --tag pravum:0.1 .

4. And run image for development

> docker run --env DEVELOPMENT_MODE=True -p 80:8000 pravum:0.1

5. Open browser and enter localhost


There some mistakes. I will fix them after your feedback
