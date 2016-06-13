# Application factory

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_github import GitHub

bootstrap = Bootstrap()
db = SQLAlchemy()
github = GitHub()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_message = 'auth.login'


def create_app():
    """ Creates the app and initializes the components """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'voll geheim!'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/catalog'

    app.config['GITHUB_CLIENT_ID'] = 'd73ccb593f271410d8a6'
    app.config['GITHUB_CLIENT_SECRET'] = 'b33db87574d91ec86296a1a52871e1ec66c1f69b'

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    github.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
