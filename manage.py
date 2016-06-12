#!/usr/bin/env python

# Contains the commands to initialize the database and run the application

from flask_script import Manager

from app import create_app
from app import db
from app.database_initialization import initialize_database

app = create_app()

with app.app_context():
    db.create_all()

manager = Manager(app)


@manager.command
def init_db():
    initialize_database()


@manager.command
def start():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    manager.run()
