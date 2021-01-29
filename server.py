from os import environ
from flask import Flask
import twitterbot

app = Flask(__name__)

@app.route("/")
def home():
    twitterbot.tweet()
    return "Tweeting....."

app.run(host= '0.0.0.0', port=environ.get('PORT'))