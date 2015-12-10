class Card:
    def __init__(self, name):
        self.name = name


class Creature(Card):
    def __init__(self, name, level, strength):
        super().__init__(name)
        self.level = level
        self.base_strength = strength
        self.strength = self.base_strength

    def take_damage(self, damage):
        self.strength -= damage


class Spell(Card):
    pass


class Counter(Card):
    pass
