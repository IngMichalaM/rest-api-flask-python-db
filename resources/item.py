import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
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


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
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