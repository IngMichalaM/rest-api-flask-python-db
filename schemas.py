from marshmallow import Schema, fields

""" 
- lecture 72 - use the marshmallow schema to check and validate
    the data that the client sends us
- dump_only=True - only used to send data back to the client, 
    not used for the incoming data validation
"""


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)  # returned for GET request
    # when we receive data and pass data trough data
    # not used for validation of the fields coming from the request

    # will be included in the response
    name = fields.Str(required=True)  # must be in the json payload
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


# TODO - what kind of message the marshmellow gives us when the validation fails?
# message = "Bad request. Ensure that 'price', 'store_id' and 'name' are included in the JSON payload."

class ItemUpdateSchema(Schema):
    # either or both can be missing
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
