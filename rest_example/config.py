#  -*- coding: utf-8 -*-
# --------------------------Flask settings------------------------------------
# server and port to start flask application
FLASK_SERVER_NAME = 'localhost:9000'
# debug option for the server
FLASK_DEBUG = True
# option to enable or disable the api documentation
DOC_SETTING = True
# ----------------------------------------------------------------------------#
# --------------------------Flask Restplus settings---------------------------#
# initial doc expansion setting.accepted values are ('none', 'list' or 'full')
SWAGGER_UI_DOC_EXPANSION = 'list'
#  set this option to validate the payload with @api.expect() decorator.
RESTPLUS_VALIDATE = True
# http://flask-restplus.readthedocs.io/en/latest/mask.html?highlight=RESTPLUS_MASK_SWAGGER
# As Swagger does not permit exposing a global header once it can make
# your Swagger specifications a lot more verbose.
# You can disable this behavior by setting RESTPLUS_MASK_SWAGGER to False
RESTPLUS_MASK_SWAGGER = False
# If a request does not match any of your application’s endpoints,
#  Flask-RESTPlus will return a 404 error message with suggestions of
# other endpoints that closely match the requested endpoint.
# This can be disabled by setting ERROR_404_HELP to False in your application
# config.
ERROR_404_HELP = False
# ----------------------------------------------------------------------------#
#  SQLAlchemy settings
# --------------------------SQLAlchemy settings-------------------------------#
# The database URI that should be used for the connection.
# http://flask-sqlalchemy.pocoo.org/2.3/config/
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
# SQLALCHEMY_TRACK_MODIFICATIONS If set to True, Flask-SQLAlchemy will track
# modifications of objects and emit signals.
# The default is None, which enables tracking but issues a warning that
# it will be disabled by default in the future.
# This requires extra memory and should be disabled if not needed
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ----------------------------------------------------------------------------#
#  LDAP settings
# --------------------------LDAP settings-------------------------------#
LDAP_PROVIDER_URL = "ldap://192.168.56.16:389"
LDAP_BASE_DN = "ou=users,dc=test,dc=com"
LDAP_USER_DN = "cn={username},ou=users,dc=test,dc=com"
LDAP_RETRIVE_ATTRS = ['givenName', 'sn', 'mail', 'uid']
LDAP_ATTRS_MAP = {
    "givenName": "first_name",
    "sn": "last_name",
    "mail": "email",
    "uid": "user",
}
LDAP_SEARCH_FILTER = "uid={username}"
# ----------------------------------------------------------------------------#
