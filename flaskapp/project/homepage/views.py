from project import db
from flask import render_template, Blueprint, request
from sqlalchemy.sql import text


# home blueprint definition
homepage_blueprint = Blueprint('homepage', __name__, template_folder='templates')


@homepage_blueprint.route('/get-users/')
def get_users():

    return render_template('home.html')


@homepage_blueprint.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h2>{}</h2>'.format("Db Connection Success!")
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        head = '<h2>Something is broken.</h2>'
        return head + error_text