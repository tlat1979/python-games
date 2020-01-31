from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed, ALL_COMPLETED
from flask import render_template
from collections import namedtuple
import threading
import requests
import json


def getAllGames():
    globalGamesArr = []
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(1, 3):
        futures.append(pool.submit(requestWorker, (x)))

    wait(futures, timeout=None, return_when=ALL_COMPLETED)
    for future in as_completed(futures):
        result = future.result()
        globalGamesArr.append(result)

    def flatten(l): return [item for sublist in l for item in sublist]
    globalGamesArr = flatten(globalGamesArr)
    globalGamesArr.sort(key=lambda x: x.rating, reverse=True)
    return render_template('games.html', title='Home', gamesArr=globalGamesArr)


def requestWorker(pageIndex):
    url = "https://api.rawg.io/api/games?page_size=20&page=" + str(pageIndex)
    localGamesArr = []
    response = requests.request("GET", url)
    games = json.loads(response.text)['results']
    for oneGame in games:
        localGamesArr.append(namedtuple(
            "Game", oneGame.keys())(*oneGame.values()))
    print(pageIndex)
    return localGamesArr
