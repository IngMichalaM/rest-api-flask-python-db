import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

# Bluprints divide API into multiple segments

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
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


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id], 200
        # only returns info about store,
        # not the items, since they are kept separately
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
