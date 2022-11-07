from flask import render_template, url_for, flash, redirect
from travelblog import app, db, bcrypt
from travelblog.forms import RegistrationForm, LoginForm
from travelblog.models import User, Post


posts = [

    {
        'author': 'Jakub Kasal',
        'title': 'Blog post 1',
        'content': 'Traveling',
        'date_posted':'April 2020'
    },

    {
        'author': 'Jack Blacksmith',
        'title': 'Blog post 2',
        'content': 'Programming',
        'date_posted':'May 2020'
    }
]

# home webpage
@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template ('about.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', 
            title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggen in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', 
            title = 'Login', form = form)