from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player

class CardGame:
    def __init__(self, p1name, p2name, num_of_cards):
        self.p1name=p1name
        self.p2name=p2name
        self.num_of_cards=num_of_cards
        p1name=Player
        p2name=Player
        num_of_cards=DeckOfCards

    def new_game(self):
        game_ongoing=1
        DeckOfCards.cards_shuffle()
        Player.set_hand(self.p1name)
        Player.set_hand(self.p2name)

    def get_winner(self):
        if len(Player.self.playerhand(self.p1name)) < len(Player.self.playerhand(self.p2name)):
            game_ongoing=0
            return f"game ended, {self.p2name} is the winner!"
        elif len(Player.self.playerhand(self.p1name)) > len(Player.self.playerhand(self.p2name)):
            game_ongoing = 0
            return f"game ended, {self.p1name} is the winner!"
        elif len(Player.self.playerhand(self.p1name)) == len(Player.self.playerhand(self.p2name)):
            game_ongoing = 0
            return None