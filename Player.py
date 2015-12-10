import random

timeperturn = 90
class Player:
    def __init__(self, name):
        self.name = name
        self.board = []
        self.hand = []
        self.deck = []
        self.grave = []
        self.counters = []
        self.triggers = []
        # self.connection = getConnection()
        self.summons = 2
        self.time = 0

    # BASIC FUNCTIONS
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

    def grave_add(self, cards):
        self.grave.extend(cards)

    def grave_remove(self, cards):
        for card in cards:
            self.hand.remove(card)

    def grave_get(self):
        return self.grave

    def board_remove(self, cards):
        for card in cards:
            self.board.remove(card)

    def board_add(self, card, position=0):
        self.board.insert(position, card)

    def board_get(self):
        return self.board
