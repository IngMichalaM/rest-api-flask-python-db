from flask import Flask, request
from db import items, stores

# to run the app: flask run
# http://127.0.0.1:5000

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": stores}, 200


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id], 200
    # only returns info about store, not the items, since they are now kept separately
    except KeyError:
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


