""" Models to be used with db stuff
"""
# stdlib imports
from datetime import datetime

# flask imports
from flask_sqlalchemy import SQLAlchemy

# project imports

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    timezone = db.Column(db.String(), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reminders = db.relationship('Reminder', backref=db.backref('person', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.__dict__


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(), db.ForeignKey('person.userid'), nullable=False)
    followupUsername = db.Column(db.String(), nullable=False)
    reminderTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.String())
    sent = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<Reminder %r>' % self.__dict__


def main():
    pass

if __name__ == "__main__":
    main()
