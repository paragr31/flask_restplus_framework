# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:22:13 2018

@author: anamika
"""

import ldap
import rest_example.config as conf


class AuthLdap():
    """
    This class is used to autheticate user with ldap
    """
    def __init__(self):
        self.ldap_url = conf.LDAP_PROVIDER_URL
        self.base_dn = conf.LDAP_BASE_DN
        self.user_dn = conf.LDAP_USER_DN
        self.retrieveAttributes = conf.LDAP_RETRIVE_ATTRS
        self.searchFilter = conf.LDAP_SEARCH_FILTER
        self.searchScope = ldap.SCOPE_SUBTREE
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, False)
        self.connection = ldap.initialize(self.ldap_url)

    def searchUser(self, user, passwd):
        userDn = self.user_dn.format(username=user)
        searchFilter = self.searchFilter.format(username=user)
        result = {}
        try:
            self.connection.bind_s(userDn, passwd)
            user = self.connection.search_s(self.base_dn, self.searchScope,
                                            searchFilter,
                                            self.retrieveAttributes)
            result['SearchResult'] = user
        except Exception as e:
            result['Error'] = e

        return result

    def getUser(self, user, passwd):
        data = self.searchUser(user, passwd)
        if 'SearchResult' in data and data['SearchResult']:
            