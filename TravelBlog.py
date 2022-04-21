from flask import Flask, render_template, url_for
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


@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', 
            title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', 
            title = 'Login', form = form)

if __name__ == '__main__':
    app.run (debug = True)
