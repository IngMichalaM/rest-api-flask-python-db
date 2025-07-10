# REST API with Flask and Python in 2025
Covers the lectures from the lecture 61
- Section 4: Introduction to Docker
- Section 5: Flask-Smorest for more efficient development

Content of the stores_as_dictionaries branch 
- Dockerfile
- .flaskenv
- db.py
- new stores and items sturcure

Structure of the stores and items
- original structure - branch *main*
- new structure - dictionaries - branch *stores_as_dictionaries*

Original structure
- lists 
- directly in the app.py as global variable
- example 

``` 
stores = [
     {
         "name": "My Store",
         "items": [
             {
                 "name": "Chair",
                 "price": 15.99
             }
         ]
     }
]
```

```
{
  "items": [
    {
      "name": "Chair",
      "price": 15.99
    }
  ]
}
```

New structure
- dictionaries
- no longer as global variable in app.py
- items and stores moved to a separate file db.py

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

