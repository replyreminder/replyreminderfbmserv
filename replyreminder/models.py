""" Models to be used with db stuff
"""
# stdlib imports
from datetime import datetime

# flask imports
from flask_sqlalchemy import SQLAlchemy

# project imports

db = SQLAlchemy()


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    timezone = db.Column(db.String(), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.title


class Reminder(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    followupUsername = db.Column(db.String(), nullable=False)
    reminderTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.String())

    def __repr__(self):
        return '<Reminder %r>' % self.title


def main():
    pass

if __name__ == "__main__":
    main()
