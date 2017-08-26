class Card:
    activation = None
    trigger = None
    continuous = None
    destruction = None
    HP = 0
    STR = 1
    INT = 2
    SPD = 3

    def __init__(self, card, player):
        self.id = card['id']
        self.name = card['name']
        self.player = player


class Creature(Card):
    def __init__(self, card, player=None):
        super().__init__(card, player)
        self.rank = card['rank']
        self.race = card['race']
        self.max_stats = card['stats']
        self.stats = self.max_stats
        self.activation = card['activation']
        self.trigger = card['trigger']
        self.continuous = card['continuous']
        self.destruction = card['destruction']

    def reset_stats(self):
        self.reset_stat(self.STR)
        self.reset_stat(self.INT)
        self.reset_stat(self.SPD)

    def reset_stat(self, stat):
        self.stats[stat] = self.max_stats[stat]

    def lose_stat(self, stat, loss):
        self.stats[stat] -= loss

    def gain_stat(self, stat, gain):
        self.stats[stat] -= gain


class Spell(Card):
    def __init__(self, card, player):
        super().__init__(card, player)
        self.activation = card['activation']
        self.costs = card['costs']


class Item(Card):
    def __init__(self, card, player=None):
        super().__init__(card, player)
        self.costs = card['costs']
        self.stats = card['stats']
        self.activation = card['activation']
        self.continuous = card['continuous']
        self.destruction = card['destruction']


class Counter(Card):
    def __init__(self, card, player=None):
        super().__init__(card, player)
        self.trigger = card['trigger']
        self.continuous = card['continuous']
        self.destruction = card['destruction']
        self.optional = card['optional']
