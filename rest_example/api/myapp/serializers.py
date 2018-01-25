# -*- coding: utf-8 -*-
from flask_restplus import fields
from ..restapi import api

cr_data_input = api.model('Input Jira CR Details', {
   'jira': fields.String(required=True, description='Jira Number'),
   'cr': fields.String(required=True, description='CR Number'),
   'created_by': fields.String(required=True,
                               description='Created By User Id'),
   'updated_by': fields.String(required=True,
                               description='Updated By User Id'),
})

cr_data = api.clone('Summit CR Details', cr_data_input, {
   'id': fields.Integer(readonly=True,
                        description='The unique indetifier of a cr'),
   'created_on': fields.DateTime,
   'updated_on': fields.DateTime,
})

pagination = api.model('A page of results', {
   'page': fields.Integer(description='Number of this page of results'),
   'pages': fields.Integer(description='Total number of pages of results'),
   'per_page': fields.Integer(
           description='Number of items per page of results'),
   'total': fields.Integer(description='Total number of results'),
})

page_of_crs = api.inherit('Page of crs', pagination, {
    'items': fields.List(fields.Nested(cr_data))
})
