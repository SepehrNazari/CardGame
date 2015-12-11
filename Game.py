from Player import Player
import Event


class Winner(Exception):
    def __init__(self, winner):
        self.winner = winner

turn_time = 90

def game():
    players = [Player('Player 1'), Player('Player 2')]
    for player in players:
        # player.load_deck()
        player.deck_shuffle()
    players[0].draw(5)
    players[1].draw(1)
    turn = 0
