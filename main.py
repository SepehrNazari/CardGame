from kivy.app import App
from kivy.uix.widget import Widget

class Card(Widget):
    pass
    # should have card graphics and attribute (e.g. power/defense), cost, etc.

class Deck(Widget):
    # contains number/list of cards, functions for drawing, shuffling, etc.
	

class Hand(Widget):
    # contains number/list of cards, functions for reading/playing a card from hand

class Graveyard(Widget):
    # contains number/list of cards, fuctions for moving card from gy back to deck/hand

class CardGame(Widget):
    pass

class CardApp(App):
    def build(self):
        return CardGame()

if __name__ == '__main__':
    CardApp().run()