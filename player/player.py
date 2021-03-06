from .discard import Discard

class Player(object):
    def __init__(self):
        self.hand = None
        self.deck = None
        self.discard_pile = Discard()
        self.board = None

    def draw(self):
        if len(self.deck) <= 0:
            raise Exception("Deck is empty, can't draw")

        card = self.deck.draw()
        self.hand.add(card)

    def discard(self, card):
        if card in self.hand:
            self.hand.remove(card)
        elif card in self.deck:
            self.deck.remove(card)
        elif card in self.board:
            self.board.remove(card)

        self.discard_pile.discard(card)
