from . import microsoft, nintendo, steam

def parse_all():
    all_games = list()
    all_games.extend(microsoft.get_all())
    all_games.extend(nintendo.get_all())
    all_games.extend(steam.get_all())

    return all_games


def parse_one(name):
    info = microsoft.get_one(name)
    if info:
        return info
    info = nintendo.get_one(name)
    if info:
        return info
    info = steam.get_one(name)
    if info:
        return info

    raise Exception()
