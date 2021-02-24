import random
from blackjack_card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(value) for i in range(4) for value in ["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)
