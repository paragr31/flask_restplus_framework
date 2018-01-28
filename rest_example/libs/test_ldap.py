# -*- coding: utf-8 -*-
import ldap

def get_ldap_connection(username, password):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, False)
    conn = ldap.initialize("ldap://192.168.56.16:389")
    base_dn = "ou=users,dc=test,dc=com"
    user_dn = "cn="+username+",ou=users,dc=test,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = ['givenName', 'sn', 'mail', 'uid']
    searchFilter = "uid="+username
    result = ""
    try:
        conn.bind_s(user_dn, password)
        result = conn.search_s(base_dn, searchScope, searchFilter,
                               retrieveAttributes)
    except Exception as e:
        print("Error :", e)

    return result


result = get_ldap_connection("paragr", "admin1234")
print(result)
