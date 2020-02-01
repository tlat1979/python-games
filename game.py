from flask import render_template
from collections import namedtuple
import requests
import json

def getOneGame(id):
    url = "https://api.rawg.io/api/games/"+str(id)
    response = requests.request("GET", url)
    game = json.loads(response.text)
    namedtuple("Game", game.keys())(*game.values())
    return render_template('game.html', title='Home', game=game)
