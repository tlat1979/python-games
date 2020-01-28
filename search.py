from flask import render_template, request
import requests
import json


def searchGame():
    gameName = request.args.get('name')
    url = "https://api.rawg.io/api/games?search=" + gameName
    response = requests.request("GET", url)
    games = json.loads(response.text)['results']
    return render_template('games.html', title='Home', gamesArr=games)
