from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run (debug = True)
