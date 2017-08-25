class Card:
    activation = None
    trigger = None
    continuous = None
    destruction = None

    def __init__(self, card, player):
        self.id = card['id']
        self.name = card['name']
        self.player = player


class Creature(Card):
    def __init__(self, card, player=None):
        super().__init__(card, player)
        self.rank = card['rank']
        self.race = card['race']
        self.max_health = card['health']
        self.health = self.max_health
        self.max_power = card['power']
        self.power = self.max_power
        self.max_magic = card['magic']
        self.magic = self.max_magic
        self.max_cunning = card['cunning']
        self.cunning = self.max_cunning
        self.activation = card['activation']
        self.trigger = card['trigger']
        self.continuous = card['continuous']
        self.destruction = card['destruction']

    def reset_stats(self):
        self.reset_stat('power')
        self.reset_stat('magic')
        self.reset_stat('cunning')

    def reset_stat(self, stat):
        self.__dict__[stat] = self.__dict__['max_{}'.format(stat)]

    def lose_stat(self, stat, loss):
        self.__dict__[stat] -= loss

    def gain_stat(self, stat, gain):
        self.__dict__[stat] -= gain


class Spell(Card):
    def __init__(self, card, player):
        super().__init__(card, player)
        self.activation = card['activation']


class Item(Card):
    def __init__(self, card, player=None):
        super().__init__(card, player)
        self.health = card['health']
        self.power = card['power']
        self.magic = card['magic']
        self.cunning = card['cunning']
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
