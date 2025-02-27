import os
from flask import Flask,request
from flask_smorest import Api, Blueprint, abort
from flask_migrate import Migrate
from db import db

from resources.store import storeBlp
from resources.product import productBlp

def create_app(db_url = None):
    app = Flask(__name__)

    app.config["API_TITLE"] = "Store Stock API"
    app.config["API_VERSION"] = "v0.1"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.drop_all()
        db.create_all()

    api = Api(app)

    api.register_blueprint(storeBlp)
    api.register_blueprint(productBlp)

    

    return app