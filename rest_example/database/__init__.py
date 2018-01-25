from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from .models import SummitCrData  # noqa
    db.drop_all()
    db.create_all()
