from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
import random

class Player:
    def __init__(self, name, num_of_cards = 26):
        self.name=name
        self.num_of_cards=num_of_cards
        if num_of_cards > 26 and num_of_cards < 10:
            self.num_of_cards=26
        self.playerhand= []

    def set_hand(self):
        if len(self.playerhand) < self.num_of_cards:
            self.playerhand.append(DeckOfCards.deal_one())

    def get_card(self):
        rand_hand=random.shuffle(self.playerhand)
        return rand_hand.pop()

    def add_card(self, v, s):
        self.playerhand.append(Card(v,s))

    def __str__(self):
        return f"Playerhand: {self.playerhand}"

    def __repr__(self):
        return f"Playerhand: {self.playerhand}"