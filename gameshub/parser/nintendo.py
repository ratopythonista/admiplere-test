from uuid import uuid4

import requests

URL = "http://192.168.68.109:5002"
PATH = "/nintendo/api/v3/portal/games/basic"

def get_all():
    games = list()
    headers = {"Authorization": "Bearer AbCdEf123456"}
    response: list[dict] = requests.get(f"{URL}{PATH}", headers=headers).json()
    for game in response:
        games.append(
            {"uuid": str(uuid4()), "short_description": game.get("shortDescription")}
        )
    return games

def get_one(name):
    headers = {"Authorization": "Bearer AbCdEf123456"}
    response: list[dict] = requests.get(f"{URL}{PATH}", headers=headers).json()
    for game in response:
        if game.get("title") == name:
            return {"uuid": str(uuid4()), "long_description": game.get("longDescription")}