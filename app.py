from flask import Flask, request
from games import getAllGames
from home import getHomePage
from search import searchGame
from game import getOneGame


app = Flask(__name__)


@app.route('/')
def index():
    return getHomePage()

@app.route('/games')
def games():
    id = request.args.get('id')
    if id is not None:
        return getOneGame(id)
    return getAllGames()

@app.route('/games/<int:id>', strict_slashes=False)
def oneGame(id):
    return 

@app.route('/search')
def search():
    return searchGame()
