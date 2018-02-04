# -*- coding: utf-8 -*-
from flask_restplus import reqparse

login_arguments = reqparse.RequestParser()
login_arguments.add_argument('username', type=str, required=True, \
                             help='User Name')
login_arguments.add_argument('password', type=pass)
