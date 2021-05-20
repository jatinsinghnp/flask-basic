

from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():
    return "<h3>hellow world</h3>"


@app.route('/service')
def service():
    return "<h1>test service</h1>"

