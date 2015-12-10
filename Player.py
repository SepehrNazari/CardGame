import random


class Player:
    def __init__(self, name):
        self.name = name
        self.board = []
        self.hand = []
        self.deck = []
        self.grave = []
        self.counters = []
        self.triggers = []

    # BASIC FUNCTIONS
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def add_bot_deck(self, card):
        self.deck.append(card)

    def add_top_deck(self, card):
        self.deck.insert(0, card)

    def shuffle_into_deck(self, card):
        self.add_bot_deck(card)
        self.shuffle_deck()
    
    def get_top_deck(self, num):
        cards = list()
        for x in range(num):
            cards.append(self.deck.pop(0))
        return cards
    
    def add_to_hand(self, cards):
        self.hand.extend(cards)

    def draw(self):
        cards = self.get_top_deck(1)
        self.add_to_hand(cards)

    def send_to_grave(self, cards):
        self.grave.extend(cards)

    def remove_from_board(self, card):
        self.board.remove(card)


