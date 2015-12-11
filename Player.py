import random

timeperturn = 90
class Player:
    def __init__(self, name):
        self.name = name
        self.board = []
        self.hand = []
        self.deck = []
        self.graveyard = []
        self.counters = []
        self.triggers = []
        # self.connection = getConnection()
        self.summons = 2

    # BASIC FUNCTIONS
    def deck_load(self):
        pass  # use mysql to load deck

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def deck_shuffle_into(self, cards):
        for card in cards:
            self.deck_add_bot(card)
        self.deck_shuffle()

    def deck_add_bot(self, cards):
        self.deck.extend(cards)

    def deck_add_top(self, cards):
        for card in cards.reverse():
            self.deck.insert(0, card)
    
    def deck_get_top(self, num):
        cards = list()
        for x in range(num):
            cards.append(self.deck.pop(0))
        return cards
    
    def hand_add(self, cards):
        self.hand.extend(cards)

    def hand_remove(self, cards):
        for card in cards:
            self.hand.remove(card)

    def hand_get(self):
        return self.hand

    def draw(self, num):
        cards = self.deck_get_top(num)
        self.hand_add(cards)

    def graveyard_add(self, cards):
        self.graveyard.extend(cards)

    def graveyard_remove(self, cards):
        for card in cards:
            self.hand.remove(card)

    def graveyard_get(self):
        return self.graveyard

    def board_remove(self, cards):
        for card in cards:
            self.board.remove(card)

    def board_add(self, card, position=0):
        self.board.insert(position, card)

    def board_get(self):
        return self.board
