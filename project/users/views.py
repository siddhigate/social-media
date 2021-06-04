from functools import wraps
from flask import (flash, redirect, render_template,
    request, session, url_for, Blueprint, logging)
from sqlalchemy.exc import IntegrityError

from .forms import RegisterForm
from project import db
from project._config import ALLOWED_EXTENSIONS
from project.models import User, Post, likes
from project.grapher import Graph
from project.RecoWithWeight import RecoWithWeight
from project.trie import Trie

from passlib.hash import sha256_crypt
import os
from werkzeug.utils import secure_filename
from functools import wraps

users_blueprint = Blueprint('users', __name__)

graph = Graph()
recowithweight = RecoWithWeight()
trie = Trie()

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

@users_blueprint.route('/')
def home():
    users_all = User.query.all()
    posts = Post.query.filter_by(comment=None).all()
    follow_suggestions = []
    if current_user():
        recowithweight.add_connection(current_user().id, 0)
        for usr in users_all:
            to_whom_followed = usr.followed.all()
            to_whom_liked = usr.likes.all()
            for followed in to_whom_followed:
                print(followed.id)
                recowithweight.add_connection(usr.id, followed.id)

        for one_suggestion in recowithweight.get_people_you_may_know(current_user().id):
            follow_suggestions.append(User.query.filter_by(id=one_suggestion).first())
    if current_user(): 
        if current_user() in follow_suggestions: 
            follow_suggestions.remove(current_user())
    return render_template('home.html', posts=posts, user=current_user(), Post_model=Post, likes=likes, follow_suggestions=follow_suggestions, User=User)

@users_blueprint.route('/home_following')
@is_logged_in
def home_following():
    posts = []
    follow_suggestions = User.query.all()
    follows = current_user().followed.all()

    for follow in follows: 
        user_posts = Post.query.filter_by(author=follow)
        posts += user_posts
    posts.sort(key=lambda r: r.date_posted) 

    if current_user():  
        if current_user() in follow_suggestions: 
            follow_suggestions.remove(current_user())

    return render_template('home.html', posts=posts, user=current_user(), Post_model=Post, likes=likes, follow_suggestions=follow_suggestions, User=User)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data.lower()
        user = User(username=username, email=email, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered and can log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].lower()
        password_candidate = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user != None:
            password = user.password
            if password_candidate == password:
                session['logged_in'] = True
                session['username'] = user.username
                session['user_id'] = user.id

                flash('You are now logged in', 'success')
                return redirect(url_for('users.home'))
            else:
                error = 'Invalid password'
                return render_template('login.html', error=error)
        else:
            error = 'Email not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

@users_blueprint.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('users.login'))

@users_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search']
        for post in Post.query.all():
            trie.insert(post.content)
        posts = []
        for found_one in trie.words_with_prefix(query):
            posts.append(Post.query.filter_by(content=found_one).first())

        return render_template('results.html', posts=posts, Post_model=Post, user=current_user(), query=query)

@users_blueprint.route('/profile')
@is_logged_in
def profile():
    profile_pic = url_for(
        'static', filename='profile_pics/' + current_user().image_file)
    return render_template('profile.html', profile_pic=profile_pic)
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@users_blueprint.route('/update_photo', methods=['GET', 'POST'])
@is_logged_in
def update_photo():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'danger')
            return redirect(url_for('users.update_photo'))
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(url_for('users.update_photo'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            current_user().image_file = filename
            db.session.commit()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(
                f'Succesfully changed profile picture to {filename}', 'success')
            return redirect(url_for('users.profile'))
    return render_template('update_photo.html', user=current_user())

@users_blueprint.route('/follow/<id>')
@is_logged_in
def follow(id):
    user_following = current_user()
    user_followed = User.query.filter_by(id=id).first()

    if user_following == user_followed:
        flash('You cant follow yourself -_-', 'danger')
        return redirect(url_for('users.home'))
    else:
        user_following.followed.append(user_followed)
        db.session.commit()
        flash(f'Followed {user_followed.username}', 'success')
        return redirect(url_for('users.home'))

@users_blueprint.route('/unfollow/<id>')
@is_logged_in
def unfollow(id):
    user_unfollowing = current_user()
    user_unfollowed = User.query.filter_by(id=id).first()

    if user_unfollowing == user_unfollowed:
        flash('You cant unfollow yourself -_-', 'danger')
        return redirect(url_for('users.home'))
    else:
        user_unfollowing.followed.remove(user_unfollowed)
        db.session.commit()
        flash(f'Unfollowed {user_unfollowed.username}', 'warning')
        return redirect(url_for('users.home'))