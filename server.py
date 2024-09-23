from flask import Flask, jsonify, request, render_template, redirect, session
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)


@app.route("/")
def home():
    return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)