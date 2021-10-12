from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    print("0ops:print")
    logging.error("0ops:logging.error")
    return "Hello, World!"
