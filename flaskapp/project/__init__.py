from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
#from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# config
app.config.from_object('config.DevelopmentConfig')
#app.config.from_object('config.ProductionConfig')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
# create the sqlalchemy object
db = SQLAlchemy(app)
# <meta name="csrf-token" content="{{ csrf_token() }}"> in jinja template
# CSRFProtect(app)


# import blueprints
from project.homepage.views import homepage_blueprint
from project.json.views import json_blueprint


app.register_blueprint(homepage_blueprint)
app.register_blueprint(json_blueprint)

# session header options:
#app.config.update(
#    SESSION_COOKIE_SECURE=False,
#    SESSION_COOKIE_HTTPONLY=True,
#    SESSION_COOKIE_SAMESITE='Lax',
#)
