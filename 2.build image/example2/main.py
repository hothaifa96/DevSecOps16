from flask import Flask

app = Flask(__name__)

@app.get('/')
def welcome_page():
    return "<h1> Welcome to my website! </h1>"


app.run(port=80,host='0.0.0.0')
