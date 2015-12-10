import Player
import Event


class Winner(Exception):
    def __init__(self, winner):
        self.winner = winner


players = [Player('Player 1'), Player('Player 2')]

def game():
    pass