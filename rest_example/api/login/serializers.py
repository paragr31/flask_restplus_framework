# -*- coding: utf-8 -*-
from flask_restplus import fields
from ..restapi import api

login_params = api.model('Login Details', {
    'username': fields.String(required=True, description='User Name'),
    'password': fields.String(required=True, description='Password')
})

user_details = api.model('User Details', {
    'username': fields.String(required=True, description='User Name'),
    'first_name': fields.String(required=True, description='First Name'),
    'last_name': fields.String(required=True, description='Last Name'),
    'email': fields.String(required=True, description='Email'),
})
