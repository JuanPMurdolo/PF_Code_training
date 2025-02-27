from db import db

class ProductStoreModel(db.Model):
    __tablename__ = 'product_store'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
