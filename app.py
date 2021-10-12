from flask import Flask, request
import logging, json
app = Flask(__name__)

@app.route("/")
def hello():
    logging.error(json.dumps(request))
    return "Hello, World!"
