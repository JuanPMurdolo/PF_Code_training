from db import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    stock = db.Column(db.Integer)
    stores = db.relationship('StoreModel', secondary='product_store', back_populates='products')