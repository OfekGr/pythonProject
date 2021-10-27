
class Card:

    def __init__(self, value, suit):
        self.value=value
        self.suit=suit


    def __gt__(self, current_card, other_card):
        if current_card.value > other_card.value:
            return True
        elif current_card.value == other_card.value:
            if current_card.suit > other_card.suit:
                return True
            else:
                return False
        else:
            return False
