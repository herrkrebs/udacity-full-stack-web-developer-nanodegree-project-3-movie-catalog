# Application factory

import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_github import GitHub
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
github = GitHub()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_message = 'auth.login'


def create_app():
    """ Creates the app and initializes the components """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get(
        'catalog_secret_key') or 'voll geheim!'
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://catalog@localhost/catalog'

    app.config['GITHUB_CLIENT_ID'] = os.environ.get('catalog_github_client_id')
    app.config['GITHUB_CLIENT_SECRET'] = os.environ.get(
        'catalog_github_client_secret')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    github.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
