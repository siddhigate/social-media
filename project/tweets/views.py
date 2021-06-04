import datetime
from functools import wraps
from flask import (flash, redirect, render_template,
    request, session, url_for, Blueprint)
from sqlalchemy.exc import IntegrityError

from project import db
from .forms import PostForm
from project.models import User, Post, likes

from passlib.hash import sha256_crypt
import os
from werkzeug.utils import secure_filename
from functools import wraps

tweets_blueprint = Blueprint('tweets', __name__)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('users.login'))
    return wrap

def current_user():
    if len(session) > 0:
        return User.query.filter_by(username=session['username']).first()
    else:
        return None

@tweets_blueprint.route('/post/<int:id>')
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', id=id, post=post, Post_model=Post, user=current_user())

@tweets_blueprint.route('/new_post/', methods=['GET', 'POST'])
@is_logged_in
def new_post():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        content = form.content.data
        post = Post(content=content, author=current_user())
        db.session.add(post)
        db.session.commit()
        flash('Your new post has been created!  😊', 'success')
        return redirect(url_for('users.home'))
    return render_template('new_post.html', form=form, title='New post')

@tweets_blueprint.route('/like/<id>')
@is_logged_in
def like_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        flash(f"Post '{id}' not found", 'warning')
        return redirect(url_for('users.home'))
    if current_user() in post.likes.all():
        post.likes.remove(current_user())
        db.session.commit()
        return redirect(url_for('users.home', _anchor=id))
    else:
        post.likes.append(current_user())
        db.session.commit()
        return redirect(url_for('users.home', _anchor=id))

@tweets_blueprint.route('/retweet/<id>')
@is_logged_in
def retweet(id):
    re_post = Post.query.filter_by(id=id).first()
    if re_post.retweet != None:
        flash("You can't retweet a retweeted tweet :(", 'danger')
        return redirect(url_for('users.home'))
    if Post.query.filter_by(user_id=current_user().id).filter_by(retweet=id).all():
        rm_post = Post.query.filter_by(
            user_id=current_user().id).filter_by(retweet=id).first()
        db.session.delete(rm_post)
        db.session.commit()

        flash('Unretweeted successfully', 'warning')
        return redirect(url_for('users.home'))

    post = Post(content='', user_id=current_user().id, retweet=id)
    db.session.add(post)
    db.session.commit()
    flash('Retweeted successfully', 'success')
    return redirect(url_for('users.home'))

@tweets_blueprint.route('/new_comment/<post_id>', methods=['GET', 'POST'])
@is_logged_in
def new_comment(post_id):
    commented_post = Post.query.filter_by(id=post_id).first()
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        content = f'@{commented_post.author.username}  ' + form.content.data
        comment = Post(content=content, author=current_user(), comment=post_id)
        db.session.add(comment)
        db.session.commit()
        flash(
            f"You have replied to {commented_post.author.username}'s tweeet", 'success')
        return redirect(url_for('users.home'))
    return render_template('new_post.html', form=form, title=f"Comment to @{commented_post.author.username}'s tweeet:")