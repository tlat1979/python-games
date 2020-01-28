from flask import Flask
from games import getAllGames
from home import getHomePage

app = Flask(__name__)


@app.route('/')
def index():
    return getHomePage()


@app.route('/games')
def games():
    return getAllGames()
