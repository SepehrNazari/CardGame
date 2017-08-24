class Account:
    def __init__(self, name):
        self.name = name
        self.odeck = []
        self.mdeck = []

    def add_to_odeck(self, cardlist):
        self.odeck.append(cardlist)

    def add_to_mdeck(self, cardlist):
        self.mdeck.append(cardlist)