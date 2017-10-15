# stdlib imports
import os

# flask imports
from flask import Flask,  jsonify
from flask_restful import reqparse
from flask_cors import CORS
from flask_autodoc import Autodoc

# sql exceptions
from sqlalchemy import exc

# project imports
from replyreminder.models import db, Person, Reminder

# app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
CORS(app)
db.init_app(app)
auto = Autodoc(app)

with app.app_context():
    db.create_all()

# parser args
parser = reqparse.RequestParser()
parser.add_argument('userid')
parser.add_argument('email')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('timezone')
parser.add_argument('updated_time')
parser.add_argument('followupUsername')
parser.add_argument('reminderTime')
parser.add_argument('notes')

@app.route("/")
def test():
    return auto.html()


@app.route("/user/", methods=['POST'])
@auto.doc()
def createUser():
    """
    Json input {userid int, email string, first_name string, last_name string, timezone string, updated_timedatetime}
    Responses 200 user successfully created or already exists, 400 malformed json input, 500 who knows?
    """
    args = parser.parse_args()
    if not args['userid']:
        return jsonify(success=False), 400

    if Person.query.filter_by(userid=args['userid']).first():
        return jsonify(success=True), 200

    try:
        db.session.add(Person(userid=args['userid'], email=args['email'],
                            first_name=args['first_name'], last_name=args['last_name'],
                            timezone=args['timezone'], updated_time=args['updated_time']))
        db.session.commit()
    except exc.IntegrityError as e:
        # Malformed Entry
        print(e)
        return jsonify(success=False), 400

    except Exception as e:
        print(e)
        return jsonify(success=False), 500

    return jsonify(success=True), 200


@app.route("/reminder/", methods=['POST'])
@auto.doc()
def createReminder():
    """
    :return:
    """
    args = parser.parse_args()
    if not args['userid']:
        return jsonify(success=False), 400

    if not Person.query.filter_by(userid=args['userid']).first():
        return jsonify(success=False), 400

    try:
        # todo: find some super cool way to do this
        db.session.add(Reminder(userid=args['userid'], followupUsername=args['followupUsername'],
                                       reminderTime=args['reminderTime'], notes=args['notes']))
        db.session.commit()

    except exc.IntegrityError as e:
        # Malformed Entry
        print(e)
        return jsonify(success=False), 400

    except Exception as e:
        print(e)
        return jsonify(success=False), 500

    return jsonify(success=True), 200


def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()