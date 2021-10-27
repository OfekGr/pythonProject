class Card:
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit

    def __gt__(self, current_card, other_card):
        if current_card > other_card:
            return True
        else:
            return False