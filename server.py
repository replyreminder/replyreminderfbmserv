# stdlib imports
import os

# flask imports
from flask import Flask,  jsonify
from flask_restful import reqparse
from flask_cors import CORS

# project imports
from replyreminder.models import db

# app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
CORS(app)
db.init_app(app)

# parser args
parser = reqparse.RequestParser()
parser.add_argument('userid')
parser.add_argument('email')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('timezone')
parser.add_argument('updated_time')
parser.add_argument('followupUser')
parser.add_argument('reminderTime')

@app.route("/")
def test():
    return jsonify(success=True), 200


@app.route("/user/", methods=['POST'])
def createUser():
    """
    :return:
    """
    args = parser.parse_args()

    return jsonify(success=True), 200


@app.route("/reminder/", methods=['POST'])
def createReminder():
    """
    :return:
    """
    args = parser.parse_args()
    return jsonify(success=True), 200


def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()