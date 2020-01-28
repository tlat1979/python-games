from flask import Flask
from games import getAllGames
from home import getHomePage
from search import searchGame


app = Flask(__name__)


@app.route('/')
def index():
    return getHomePage()


@app.route('/games')
def games():
    return getAllGames()


@app.route('/search')
def search():
    return searchGame()
