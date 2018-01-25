# -*- coding: utf-8 -*-
from database import db
from database.models import SummitCrData


def create_cr_data(data):
    jira = data.get('jira')
    cr = data.get('cr')
    created_by = data.get('created_by')
    updated_by = data.get('updated_by')
    crData = SummitCrData(jira, cr, created_by, updated_by)
    db.session.add(crData)
    db.session.commit()


def update_cr_data(jira, data):
    crData = SummitCrData.query.filter(SummitCrData.jira == jira).one()
    crData.cr = data.get('cr')
    crData.updated_by = data.get('updated_by')
    db.session.add(crData)
    db.session.commit()


def delete_cr_data(jira):
    crData = SummitCrData.query.filter(SummitCrData.jira == jira).one()
    db.session.delete(crData)
    db.session.commit()
