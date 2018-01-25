# -*- coding: utf-8 -*-
from flask_restplus import reqparse

cr_arguments = reqparse.RequestParser()
cr_arguments.add_argument('page', type=str, required=False, help='Page Number')
cr_arguments.add_argument('bool', type=bool, required=False, default=1,
                          help='Page number')
cr_arguments.add_argument('per_page', type=int, required=False,
                          choices=[2, 10, 20, 30, 40, 50],
                          default=10, help='Results per page {error_msg}')
