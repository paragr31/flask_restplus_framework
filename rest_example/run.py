# -*- coding: utf-8 -*-
import logging.config
import sys
import platform

path = "C:\\PARAG\\PythonProgramms\\rest_example"

if platform.system() == "Windows" and path not in sys.path:
    sys.path.append(path)

from os import path
from flask import Flask, Blueprint
from rest_example import config
from rest_example.api.myapp.views import ns as crs_namespace
from rest_example.api.restapi import api
from rest_example.database import db

app = Flask(__name__)

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = config.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = config.SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = config.ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(crs_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(port=9000, debug=config.FLASK_DEBUG)


if __name__ == "__main__":
    main()