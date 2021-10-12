from flask import Flask, request
import logging, json
app = Flask(__name__)

@app.route("/")
def hello():
    logging.error(request)
    logging.error(request.headers)
    logging.error(request.remote_addr)
    return "Hello, World!"
