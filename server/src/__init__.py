from flask import Flask, request, render_template
from flask_jwt_extended import JWTManager
import mongoengine as me

from .models import create_models
from .views import create_api_views, create_users_api_views
from .handlers import create_handlers


def create_app():
    app = Flask(__name__)
    return app


def create_db():
    models = create_models(me)
    me.connect('popular_admin_db')  # TODO: add config options
    return models


def add_routes(app, request, handlers):
    api = create_api_views(handlers, request)
    users_api = create_users_api_views(handlers, request)
    app.register_blueprint(api, url_prefix='/api/v1')
    app.register_blueprint(users_api, url_prefix='/api/v1/users')


def build_app():
    app = create_app()
    app.secret_key = 'fajdsklfakçdlfadbghakjdnjs'
    jwt = JWTManager(app)
    models = create_db()
    handlers = create_handlers(models)
    add_routes(app, request, handlers)

    return app
