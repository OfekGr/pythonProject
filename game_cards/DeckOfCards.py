from game_cards.Card import Card
import random

class DeckOfCards:
    def __init__(self):
        self.cards= []
        for v in range (2,15):
            for s in range(4):
                self.cards.append(Card(v,s))


    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return random.choice.cards_shuffle()

    def __str__(self):
        return f"cards in hand: {self.cards}"

    def __repr__(self):
        return f"cards in hand: {self.cards}"
