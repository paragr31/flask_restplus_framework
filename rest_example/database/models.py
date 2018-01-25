# -*- coding: utf-8 -*-
from datetime import datetime
from database import db


class SummitCrData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jira = db.Column(db.String(100))
    cr = db.Column(db.String(100))
    created_by = db.Column(db.String(80))
    created_on = db.Column(db.DateTime)
    updated_by = db.Column(db.String(80))
    updated_on = db.Column(db.DateTime)

    def __init__(self, jira, cr, created_by, updated_by, created_on=None,
                 updated_on=None):
        self.jira = jira
        self.cr = cr
        self.created_by = created_by
        self.updated_by = updated_by
        if created_on is None:
            created_on = datetime.utcnow()
        if updated_on is None:
            updated_on = datetime.utcnow()
        self.created_on = created_on
        self.updated_on = updated_on

    def __repr__(self):
        return '<SummitCrData %r>' % self.cr
