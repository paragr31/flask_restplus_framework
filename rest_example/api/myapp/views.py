# -*- coding: utf-8 -*-
import logging
from flask import request
from flask_restplus import Resource
from .business import create_cr_data, update_cr_data, delete_cr_data
from .serializers import cr_data, page_of_crs, cr_data_input
from .parsers import cr_arguments
from api.restapi import api
from database.models import SummitCrData

log = logging.getLogger(__name__)

ns = api.namespace('jira/crdetails',
                   description='Operations Related to Jira CRs')


@ns.route("/")
class CrCollection(Resource):

    @api.expect(cr_arguments)
    @api.marshal_with(page_of_crs)
    def get(self):
        """
        Returns list of cr's
        """
        args = cr_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        crs_query = SummitCrData.query
        crs_page = crs_query.paginate(page, per_page, error_out=False)

        return crs_page

    @api.expect(cr_data_input)
    def post(self):
        """
        Creates New Entry for Jira and its CR Details
        """
        create_cr_data(request.json)
        return None, 201


@ns.route('/<string:jira>')
@api.response(404, 'Jira not found.')
class JiraCrItem(Resource):

    @api.marshal_with(cr_data, as_list=True)
    def get(self, jira):
        """
        Returns a jira item.
        """
        log.info(str(SummitCrData.query.filter(
                        SummitCrData.jira == jira).one()))
        return SummitCrData.query.filter(SummitCrData.jira == jira).one()

    @api.expect(cr_data_input)
    @api.response(204, 'Post successfully updated.')
    def put(self, jira):
        """
        Updates a Jira Detail.
        """
        update_cr_data(jira, request.json)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, jira):
        """
        Deletes a jira detail.
        """
        delete_cr_data(jira)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class JiraCrsArchiveCollection(Resource):

    @api.expect(cr_arguments, validate=True)
    @api.marshal_with(page_of_crs)
    def get(self, year, month=None, day=None):
        """
        Returns list of jiras from a specified time period.
        """
        args = cr_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month,
                                                      start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        crs_query = SummitCrData.query.filter(
                    SummitCrData.created_on >= start_date).filter(
                    SummitCrData.created_on <= end_date)
        crs_page = crs_query.paginate(page, per_page, error_out=False)

        return crs_page
