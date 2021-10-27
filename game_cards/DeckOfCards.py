from game_cards.Card import Card
import random

class DeckOfCards:
    def __init__(self):
        self.cards= []
        for v in range(13):
            for s in range(4):
                self.cards.append(Card(v,s))

    def cards_shuffle(self):
        return random.shuffle(self.cards)

    def deal_one(self):
        removed_card=self.cards.pop(random.choice(self.cards_shuffle()))
        return removed_card

    def __str__(self):
        return f"cards in hand: {self.cards}"

    def __repr__(self):
        return f"cards in hand: {self.cards}"