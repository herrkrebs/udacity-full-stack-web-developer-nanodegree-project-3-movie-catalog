# Contains the main routes

from flask import render_template, redirect, request, flash, jsonify, url_for
from flask_login import login_required

from app.main.forms import MovieForm
from . import main
from .. import db
from ..models import Genre, Movie


@main.route('/')
@main.route('/catalog')
def index():
    genres = Genre.query.order_by('name asc').all()
    latest_movies = Movie.query.order_by('id desc').limit(10).all()
    return render_template('movies.html', genres=genres, movies=latest_movies)


@main.route('/catalog/<genre_name>/movies')
def movies(genre_name):
    genres = Genre.query.order_by('name asc').all()
    movies = Movie.query.filter_by(genre_name=genre_name).all()
    return render_template('movies.html', genre_name=genre_name, genres=genres,
                           movies=movies)


@main.route('/catalog/<genre_name>/<movie_title>')
def movie(genre_name, movie_title):
    movie = Movie.query.filter_by(title=movie_title).one()
    return render_template('movie.html', movie=movie)


@main.route('/catalog/<genre_name>/new', methods=['GET', 'POST'])
@login_required
def create_movie(genre_name):
    form = MovieForm()

    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            description=form.description.data,
            year=form.year.data,
            image_url=form.image.data,
            genre_name=genre_name
        )

        db.session.add(new_movie)
        db.session.commit()

        flash("New Movie added!")

        return redirect(url_for('main.movies', genre_name=genre_name))

    return render_template('create_movie.html', genre_name=genre_name,
                           form=form)


@main.route('/catalog/<movie_title>/edit', methods=['GET', 'POST'])
@login_required
def edit_movie(movie_title):
    movie = Movie.query.filter_by(title=movie_title).one()

    form = MovieForm()

    if form.validate_on_submit():
        movie.title = form.title.data
        movie.description = form.description.data
        movie.year = form.year.data
        movie.image_url = form.image.data

        db.session.add(movie)
        db.session.commit()

        flash('Movie edited!')

        return redirect(url_for('main.movies', genre_name=movie.genre_name))

    form.title.data = movie.title
    form.description.data = movie.description
    form.image.data = movie.image_url
    form.year.data = movie.year

    return render_template('edit_movie.html', movie=movie, form=form)


@main.route('/catalog/<movie_title>/delete', methods=['GET', 'POST'])
@login_required
def delete_movie(movie_title):
    movie = Movie.query.filter_by(title=movie_title).one()
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()

        flash('Movie deleted!')

        return redirect(url_for('main.movies', genre_name=movie.genre_name))
    else:
        return render_template('delete_movie.html', movie=movie)


@main.route('/catalog.json')
def get_json():
    """ Generates a json response of the genres and their movies """
    genres = Genre.query.all()
    return jsonify(Genres=[g.serialize for g in genres])
