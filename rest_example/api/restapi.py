# -*- coding: utf-8 -*-
import logging
import traceback

from flask_restplus import Api
from rest_example import config
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

set_doc = config.DOC_SETTING

if set_doc:
    api = Api(version='1.0', title='My Rest Example',
              description="A Simple Demonstration of Flask RESTAPI with doc")
else:
    api = Api(version='1.0', title='My Rest Example', doc=False,
              description="A Simple Demonstration of Flask RESTAPI with doc")


@api.errorhandler
def default_error_handler(e):
    message = 'An unexpected exception occured.'
    log.exception(message)

    if not config.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was not found.'}, 404
