# REST APUI with Flask and Python in 2025
Covers the lectures 52-60 - Section 3: Your first REST API

## Install requirements.txt
 `pip install -r requirements.txt`
 
## Run Flask
`flask run`

## Create docker image
 `docker build -t rest-api-flask-python .`
 - -t - tag
 - rest-api-flask-python - name
 - . location of tje Dockerfile - current directory

## Problems with docker authentication
0. `docker logout`
1. `docker login -u <docker username>`
2. At the password prompt, enter the personal access token.

## Run docker from command line
 `docker run -p 5000:5000 rest-api-flask-python`

