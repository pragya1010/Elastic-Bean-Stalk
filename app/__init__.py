from flask import Flask

application = Flask(__name__, static_url_path='/app/static')
application.config['SECRET_KEY'] = 'Pragya'

from app import routes
