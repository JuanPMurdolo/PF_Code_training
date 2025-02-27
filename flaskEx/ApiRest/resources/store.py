from flask_smorest import Api, Blueprint, abort
from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from models import product, store, product_store
from schemas import ProductSchema, StoreSchema, ProductStoreSchema, ProductPlainDataSchema, StorePlainDataSchema
from db import db

storeBlp = Blueprint('store', 'store', url_prefix='/store')

@storeBlp.route('/')
class StoreList(MethodView):
    @storeBlp.response(200, StoreSchema(many=True))
    def get(self):
        return store.StoreModel.query.all()

    @storeBlp.arguments(StorePlainDataSchema)
    @storeBlp.response(200, StoreSchema)
    def post(self, store_data):
        new_store = store.StoreModel(**store_data)
        db.session.add(new_store)
        db.session.commit()
        return new_store
    
@storeBlp.route('/<int:store_id>')
class StoreDetail(MethodView):
    @storeBlp.response(200, StoreSchema)
    def get(self, store_id):
        store_instance = store.StoreModel.query.get_or_404(store_id)
        return store_instance

    @storeBlp.arguments(StorePlainDataSchema)
    @storeBlp.response(200, StoreSchema)
    def put(self, store_data, store_id):
        store_instance = store.StoreModel.query.get_or_404(store_id)
        store_instance.update(store_data)
        db.session.commit()
        return store_instance

    @storeBlp.response(200, StoreSchema)
    def delete(self, store_id):
        store_instance = store.StoreModel.query.get_or_404(store_id)
        db.session.delete(store_instance)
        db.session.commit()
        return store_instance
    
@storeBlp.route('/<int:store_id>/products')
class StoreProducts(MethodView):
    @storeBlp.arguments(ProductPlainDataSchema)
    @storeBlp.response(200, ProductStoreSchema)
    def post(self, product_data, store_id):
        store_instance = store.StoreModel.query.get_or_404(store_id)
        product_instance = product.ProductModel(**product_data)
        product_store_instance = product_store.ProductStoreModel(product=product_instance, store=store_instance)
        db.session.add(product_store_instance)
        db.session.commit()
        return product_store_instance

    @storeBlp.response(200, ProductStoreSchema(many=True))
    def get(self, store_id):
        store_instance = store.StoreModel.query.get_or_404(store_id)
        return store_instance.products
    
@storeBlp.route('/<int:store_id>/products/<int:product_id>')
class StoreProduct(MethodView):
    @storeBlp.response(200, ProductStoreSchema)
    def get(self, store_id, product_id):
        product_store_instance = product_store.ProductStoreModel.query.filter_by(store_id=store_id, product_id=product_id).first()
        if not product_store_instance:
            abort(404, message='Product not found in store')
        return product_store_instance

    @storeBlp.response(200, ProductStoreSchema)
    def delete(self, store_id, product_id):
        product_store_instance = product_store.ProductStoreModel.query.filter_by(store_id=store_id, product_id=product_id).first()
        if not product_store_instance:
            abort(404, message='Product not found in store')
        db.session.delete(product_store_instance)
        db.session.commit()
        return product_store_instance

    @storeBlp.arguments(ProductPlainDataSchema)
    @storeBlp.response(200, ProductStoreSchema)
    def put(self, product_data, store_id, product_id):
        product_store_instance = product_store.ProductStoreModel.query.filter_by(store_id=store_id, product_id=product_id).first()
        if not product_store_instance:
            abort(404, message='Product not found in store')
        product_store_instance.update(product_data)
        db.session.commit()
        return product_store_instance
    
@storeBlp.route('/<int:store_id>/products/<int:product_id>/quantity')
class StoreProductQuantity(MethodView):
    @storeBlp.arguments(ProductPlainDataSchema)
    @storeBlp.response(200, ProductStoreSchema)
    def put(self, product_data, store_id, product_id):
        product_store_instance = product_store.ProductStoreModel.query.filter_by(store_id=store_id, product_id=product_id).first()
        if not product_store_instance:
            abort(404, message='Product not found in store')
        product_store_instance.update(product_data)
        db.session.commit()
        return product_store_instance