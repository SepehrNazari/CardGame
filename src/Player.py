import random
from src.Card import Creature, Spell, Item, Counter


class Player:
    def __init__(self, account):
        self.name = account.name
        self.odeck = account.odeck
        self.mdeck = account.mdeck
        self.board = []
        self.hand = []
        self.graveyard = []
        self.counters = []
        self.triggers = []
        self.coins = 0
        self.summons = 1

    # BASIC FUNCTIONS
    def deck_load(self):
        odeck = []
        mdeck = []
        for card in self.odeck:
            odeck.append(Creature(card, self))
        for card in self.mdeck:
            if card['type'] == 'item':
                mdeck.append(Item(card, self))
            elif card['type'] == 'spell':
                mdeck.append(Spell(card, self))
            elif card['type'] == 'counter':
                mdeck.append(Counter(card, self))
            else:
                raise Exception("Card has invalid type")
        self.odeck = odeck
        self.mdeck = mdeck

    def deck_shuffle(self, deck):
        random.shuffle(deck)

    def deck_shuffle_into(self, deck, cards):
        for card in cards:
            self.deck_add_bot(deck, card)
        self.deck_shuffle(deck)

    def deck_add_bot(self, deck, cards):
        deck.extend(cards)

    def deck_add_top(self, deck, cards):
        for card in cards.reverse():
            deck.insert(0, card)
    
    def deck_get_top(self, deck, num):
        cards = list()
        for x in range(num):
            cards.append(deck.pop(0))
        return cards
    
    def hand_add(self, cards):
        self.hand.extend(cards)

    def hand_remove(self, cards):
        for card in cards:
            self.hand.remove(card)

    def hand_get(self):
        return self.hand

    def draw(self, deck, num):
        cards = self.deck_get_top(deck, num)
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

    def gain_coins(self, coins):
        self.coins += coins
