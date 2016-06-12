# Contains the routes for user authentication

from flask import redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from .. import db, github
from ..models import User


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/login')
def login():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))

    return github.authorize(
        redirect_uri=url_for('auth.authorized', _external=True))


@auth.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = request.args.get('next') or url_for('main.index')
    if oauth_token is None:
        flash('Authorization failed.')
        return redirect(next_url)

    user = User.query.filter_by(social_id=oauth_token).first()
    if user is None:
        user = User(social_id=oauth_token)
        db.session.add(user)

    user.social_id = oauth_token
    db.session.commit()

    login_user(user, True)

    flash('You are now logged in')

    return redirect(next_url)
