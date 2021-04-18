from flask import Flask
app = Flask(__name__)

moje_imie = 'Michal'

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto')
def kto():
    return moje_imie


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

@app.route('/nowyrok')
def nowyrok():
    return '2021!'
