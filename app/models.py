# Contains the domain models of the application

from flask_login import UserMixin

from . import db, login_manager


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    movies = db.relationship('Movie', back_populates='genre')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'movies': [m.serialize for m in self.movies]
        }


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(250))
    year = db.Column(db.String(4))
    genre_name = db.Column(db.String(250), db.ForeignKey('genre.name'))
    genre = db.relationship('Genre', back_populates='movies')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image-url': self.image_url,
            'year': self.year
        }


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
