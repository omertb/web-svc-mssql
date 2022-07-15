from project import db
from flask import Blueprint, request, jsonify
from sqlalchemy.sql import text


# home blueprint definition
json_blueprint = Blueprint('json', __name__)


@json_blueprint.route('/get-users/users.json')
def get_users():
    try:
        sql_query = text('SELECT first_name, last_name, phone, email FROM sales.customers')
        #result = db.session.execute(sql_query)
        with db.engine.connect() as connection:
            result = connection.execute(sql_query)
            result_list = [dict(row) for row in result]
        return jsonify(result_list)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        head = '<h2>Something is broken.</h2>'
        return head + error_text