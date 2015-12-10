class Card:
    activation = None
    trigger = None
    continuous = None

    def __init__(self, name):
        self.name = name


class Creature(Card):
    def __init__(self, name, level, strength, activation, trigger, continuous):
        super().__init__(name)
        self.level = level
        self.base_strength = strength
        self.strength = self.base_strength
        self.activation = activation
        self.trigger = trigger
        self.continuous = continuous

    def take_damage(self, damage):
        self.strength -= damage


class Spell(Card):
    def __init__(self, name, activation):
        super().__init__(name)
        self.activation = activation


class Counter(Card):
    def __init__(self, name, trigger, continuous, optional):
        super().__init__(name)
        self.trigger = trigger
        self.continuous = continuous
        self.optional = optional
