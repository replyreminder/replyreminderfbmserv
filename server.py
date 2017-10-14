from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask import render_template, abort
from flask_restful import reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def test():
    return jsonify(success=True), 200

def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()