import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """ Get list of all the items. """
        return items.values()
        # marshmallow automatically turns the response to a list
        # list, not object as before, is returned

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        """ Add new item. """
        # - item_data - validated dictionary
        # - The json that the client passed, goes through the ItemSchema
        #   check that the fields are there, and they are valid
        #   and forward the validated dictionary
        # - Validate data type and obligatory fields present -> marshmallow schema
        # - Check duplication of the items - this is not checked by marshmallow,
        #   however will be done later on using the database

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

        return item


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """ Get particular item. """
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    # not necessary to add the decorator. It does not return anything, just the message.
    def delete(self, item_id):
        """ Delete particular item. """
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)  # order of the decorators matters
    def put(self, item_data, item_id):  # item_data goes in front of everything else
        """ Update particular item. """
        try:
            item = items[item_id]
            # update the item
            item |= item_data  # in-place union
            return item
        except KeyError:
            abort(404, message="Item not found.")