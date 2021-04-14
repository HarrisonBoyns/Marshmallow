from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.resources.store import StoreList, Store
from app.resources.user import (
    UserRegister,
    UserResource,
    UserLogin,
    TokenRefresh,
    revoked_tokens,
    UserLogOut,
    AllUsers,
)
from app.resources.items import Items, ItemList
from app.callbacks.callbacks import register_callbacks
from marshmallow import ValidationError

app = Flask(__name__)

app.secret_key = "top_secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["PROPAGATE_EXCEPTIONS"] = True


#  can set error handlers at a level - much like in springboot
@app.errorhandler(ValidationError)
def validation_error(error):
    return {
        "message" : "validation error occured",
        "error": error.messages
    }, 400

api = Api(app)

jwt = JWTManager(app)

register_callbacks(jwt)

api.add_resource(Items, "/items/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/signup")
api.add_resource(Store, "/stores/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserResource, "/users/<int:id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogOut, "/logout")
api.add_resource(AllUsers, "/users")
