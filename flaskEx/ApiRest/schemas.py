from marshmallow import Schema, fields

class ProductPlainDataSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

class ProductSchema(ProductPlainDataSchema):
    id = fields.Int(dump_only=True)

class ProductUpdateSchema(ProductPlainDataSchema):
    id = fields.Int(required=True)
    name = fields.Str(required=False)
    price = fields.Float(required=False)
    stock = fields.Int(required=False)

class ProductDeleteSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=False)
    products = fields.Nested(ProductSchema, many=True)

class StorePlainDataSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)

class StoreSchema(StorePlainDataSchema):
    id = fields.Int(dump_only=True)

class StoreUpdateSchema(StorePlainDataSchema):
    id = fields.Int(required=True)
    name = fields.Str(required=False)
    address = fields.Str(required=False)
    products = fields.Nested(ProductSchema, many=True)

class StoreDeleteSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=False)
    address = fields.Str(required=False)
    stores = fields.Nested(StoreSchema, many=True)

class OrderPlainDataSchema(Schema):
    date = fields.Str(required=True)
    total = fields.Float(required=True)

class OrderSchema(OrderPlainDataSchema):
    id = fields.Int(dump_only=True)
    products = fields.Nested(ProductSchema, many=True)

class ProductStoreSchema(Schema):
    store = fields.Nested(StoreSchema)
    product = fields.Nested(ProductSchema)