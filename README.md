# REST API with Flask and Python in 2025
Covers the lectures from the lecture 70
- Lecture 70: How to use Blueprints and MethodViews in Flask
- Lecture 71: How to write marshmallow schemas for our API
- Lecture 72: How to perform data validation with marshmallow
- Lecture 73: Decorating responses with Flask-Smorest

Data structure
- dictionaries in file db.py

``` 
stores = {}
```

``` 
items = {
    "1": {
        "name": "Chair",
        "price": 15.99
    },
    "2": {
        "name": "Croissant",
        "price": 1.25
    }
}
```

## Flask Blueprint
A Flask Blueprint is a way to organize a Flask application into smaller, modular components. It helps structure your code in a clean and scalable way, especially for larger applications.

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
or 
`docker run -dp 5000:5000 rest-api-flask-python`
to run the docker in the background and still access the command line. 


# GIT 
- log: `git --no-pager log --oneline`
- add: `git add <file name>`
- commit: `git commit -m "<message>"`
- correct commit message (interactive rebase): 
  - `git rebase -i HEAD~X` - X how many commits back to show
    - reword - edit commit message
    - fixup - like squash, but discard commit's tag (put two commits together, keeping the older commit message)
- tags: 
  - `git tag <tag name> <commit hash>`
  - list of tags: `git tag`




comments 
Lecture 70
Hi Jose, 
As you have shonw the POST /item in swagger, we don't acctually get the structure of the body from it, do we? 
And the obligatory body content. 
