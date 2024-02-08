from flask import render_template
from . import main


@main.route('/')
@main.route('/index')
def home_page():
    return render_template('index.html')

@main.route('/about')
def about_page():
    return render_template('about.html')
