from odmantic import AIOEngine, Model


class Player(Model):
    name: str
    game: str
