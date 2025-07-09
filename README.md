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
    1: {
        "name": "Chair",
        "price": 15.99
    },
    2: {
        "name": "Croissant",
        "price": 1.25
    }
}
```
