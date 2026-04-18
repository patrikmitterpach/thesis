import os

from flask import Flask

from source import database
from source import authentication
from source import monitor
from source import input





def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'reportmancer.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    

    database.init_app(app)

    app.register_blueprint(authentication.bp)
    app.register_blueprint(monitor.bp)
    app.register_blueprint(input.bp)

    app.add_url_rule('/', endpoint='index')



    return app