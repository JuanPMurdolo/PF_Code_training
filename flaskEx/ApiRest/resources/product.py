from flask_smorest import Api, Blueprint, abort
from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from models import product, store, product_store
from schemas import ProductSchema, StoreSchema, ProductStoreSchema, ProductPlainDataSchema, StorePlainDataSchema
from db import db

productBlp = Blueprint('products', 'products', url_prefix='/products')

@productBlp.route('/')
class ProductList(MethodView):
    @productBlp.response(200, ProductSchema(many=True))
    def get(self):
        return product.ProductModel.query.all()

    @productBlp.arguments(ProductPlainDataSchema)
    @productBlp.response(200, ProductSchema)
    def post(self, product_data):
        new_product = product.ProductModel(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return new_product
    
@productBlp.route('/<int:product_id>')
class ProductDetail(MethodView):
    @productBlp.response(200, ProductSchema)
    def get(self, product_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        return product_instance

    @productBlp.arguments(ProductPlainDataSchema)
    @productBlp.response(200, ProductSchema)
    def put(self, product_data, product_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        product_instance.update(product_data)
        db.session.commit()
        return product_instance

    @productBlp.response(200, ProductSchema)
    def delete(self, product_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        db.session.delete(product_instance)
        db.session.commit()
        return product_instance
    
@productBlp.route('/<int:product_id>/stores')
class ProductStores(MethodView):
    @productBlp.arguments(StorePlainDataSchema)
    @productBlp.response(200, ProductStoreSchema)
    def post(self, store_data, product_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        store_instance = store.StoreModel(**store_data)
        product_store_instance = product_store.ProductStoreModel(product=product_instance, store=store_instance)
        db.session.add(product_store_instance)
        db.session.commit()
        return product_store_instance

    @productBlp.response(200, ProductStoreSchema(many=True))
    def get(self, product_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        return product_instance.stores.all()
    
@productBlp.route('/<int:product_id>/stores/<int:store_id>')
class ProductStoreDetail(MethodView):
    @productBlp.response(200, ProductStoreSchema)
    def get(self, product_id, store_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        store_instance = product_instance.stores.filter_by(id=store_id).first_or_404()
        return store_instance

    @productBlp.response(200, ProductStoreSchema)
    def delete(self, product_id, store_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        store_instance = product_instance.stores.filter_by(id=store_id).first_or_404()
        db.session.delete(store_instance)
        db.session.commit()
        return store_instance
    
@productBlp.route('/<int:product_id>/stores/<int:store_id>/quantity')
class ProductStoreQuantity(MethodView):
    @productBlp.arguments(ProductStoreSchema)
    @productBlp.response(200, ProductStoreSchema)
    def put(self, product_store_data, product_id, store_id):
        product_instance = product.ProductModel.query.get_or_404(product_id)
        store_instance = product_instance.stores.filter_by(id=store_id).first_or_404()
        store_instance.update(product_store_data)
        db.session.commit()
        return store_instance