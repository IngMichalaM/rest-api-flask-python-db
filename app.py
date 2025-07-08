from flask import Flask, request
from db import items, stores

# to run the app: flask run
# http://127.0.0.1:5000

app = Flask(__name__)

# orig structuree
# stores = [
#     {
#         "name": "My Store",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
#     },
#     {
#         "items": [],
#         "name": "Pet Store"
#     },
#     {
#         "items": [],
#         "name": "Backery"
#     }
# ]

# new - in db.py
# stores = {}
# items = {
#     1: {
#         "name": "Chair",
#         "price": 15.99
#     },
#     2: {
#         "name": "Croissant",
#         "price": 1.25
#     }
# }


@app.get("/store")
def get_stores():
    return {"stores": stores}, 200


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return {"message": "Store not found"}, 404


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "item": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"],
                        "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}, 200
    return {"message": "Store or item not found"}, 404


