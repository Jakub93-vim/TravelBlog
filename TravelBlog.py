from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ju5df4f5669vfdvvd5'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run (debug = True)
