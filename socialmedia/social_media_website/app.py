# Author = 'Satya B'
# Version = 1.0

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm, RegistrationForm
from models import User
from database import get_user, create_user, get_posts, create_post
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
# Setting up MongoDB connection
from database import users, posts, comments, likes

# Set up Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(username):
    return User.get(username)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/post/<post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user:
            print("User",user)
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password_hash = form.password.data  # Hash the password before saving
        email = form.email.data
        full_name = form.full_name.data

        # Check if user already exists
        if get_user(username):
            flash('Username already exists. Please choose a different username.', 'danger')
            return redirect(url_for('register'))

        create_user(username, password_hash, email, full_name)
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = current_user.username
        create_post(title, content, author)
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('create_post.html')

@app.route('/posts')
def view_posts():
    posts = get_posts()
    return render_template('view_posts.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
