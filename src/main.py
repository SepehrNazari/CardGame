from src.player import Player
from src.account import Account
from src.cards import cards
from src.event import *
import random


class Game:
    def __init__(self, players):
        self.players = players
        self.turn = 0
        self.active_player = players[0]

    def start(self):
        for player in self.players:
            player.deck_load()
            player.deck_shuffle(player.odeck)
            player.deck_shuffle(player.mdeck)
            player.draw(player.odeck, 3)
            player.draw(player.mdeck, 3)
            # mulligan option

    def game(self):
        ap = self.active_player
        draw(ap, ap.odeck, 1)
        play = input("Which monster do you want to play?")
        play_card(ap, ap.hand[play], 0)
        while True:
            self.turn += 1
            ap = players[self.turn % 2]
            draw(ap, ap.odeck, 1)
            play = input("Which monster do you want to play?")
            play_card(ap, ap.hand[play], 0)
            end_turn = False
            while not end_turn:
                play = int(input("Which card do you want to play?"))
                if 0 <= play <= len(ap.hand):
                    play_card(ap, ap.hand[play], 0)
                else:
                    end_turn = True



if __name__ == '__main__':
    accounts = [Account('Player 1'), Account('Player 2')]
    accounts[0].add_to_odeck([0, 1, 2, 3, 4, 5])
    accounts[1].add_to_odeck([0, 1, 2, 3, 4, 5])
    accounts[0].add_to_mdeck([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    accounts[1].add_to_mdeck([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    players = [player(accounts[0]), accounts[1]]
    game = Game(players)
    game.start()
    game.game()
