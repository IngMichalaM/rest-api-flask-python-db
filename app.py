import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

# to run the app: flask run
# http://127.0.0.1:5000

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    # print(f"{store_data=}")
    # print(type(store_data))
    # check store name
    # check that the new store does not already exist
    if "name" not in store_data:
        abort(400,
              message="Bad request. Ensure that 'name' is included in the JSON payload.")

    for store in stores.values():
        print(store)
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists.")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    # check that all the obligatory parameters are present
    # TODO: validate data type
    if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. Ensure that 'price', 'store_id' and 'name' are included in the JSON payload."
        )

    # check duplication of the items
    for item in items.values():
        if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="Item already exists in this store.")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201


@app.get("/item")
def get_all_items():
    # print('------------------')
    # print(items)
    # print(items.values())
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id], 200
    # only returns info about store, not the items, since they are now kept separately
    except KeyError:
        abort(404, message="Store not found.")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")


# TODO: cannot delte a store where are items
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found.")


# delete item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found.")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    print(item_data)
    if "price" not in item_data or "name" not in item_data:
        abort(400,
              message="Bad request. Ensure that 'price' and 'name' are included in the JSON payload.")

    try:
        item = items[item_id]
        print(item)
        # update the item
        item |= item_data  # in-place union
        return item
    except KeyError:
        abort(404, message="Item not found.")