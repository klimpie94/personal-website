from flask import make_response, abort, render_template
from . import main


@main.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@main.route('/user/<name>')
def user(name):
    if str(name).capitalize() == "Anis":
        abort(404)
    return render_template('user.html', name=name)
