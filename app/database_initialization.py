# Initializes the database with genres and movies

from app import db
from models import Genre


def initialize_database():
    # Initialize genres
    action = Genre(name='Action')
    db.session.add(action)
    db.session.commit()

    adventure = Genre(name='Adventure')
    db.session.add(adventure)
    db.session.commit()

    thriller = Genre(name='Thriller')
    db.session.add(thriller)
    db.session.commit()

    western = Genre(name='Western')
    db.session.add(western)
    db.session.commit()

    fantasy = Genre(name='Fantasy')
    db.session.add(fantasy)
    db.session.commit()

    comedy = Genre(name='Comedy')
    db.session.add(comedy)
    db.session.commit()

    romance = Genre(name='Romance')
    db.session.add(romance)
    db.session.commit()

    sci_fi = Genre(name='Sci-Fi')
    db.session.add(sci_fi)
    db.session.commit()
