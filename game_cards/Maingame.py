from game_cards.Card import Card
from game_cards.CardGame import CardGame

game=CardGame(input("Insert gae1: "), input("Insert gae2: "), 26)
game.new_game()
print("Player name: ", game.playerOne.name, "Player cards: ",game.playerOne.playerhand)
print("Player name: ", game.playerTwo.name, "Player cards: ",game.playerTwo.playerhand)


for i in range(10):
    p1card=game.playerOne.get_card()
    p2card=game.playerTwo.get_card()
    print({game.playerOne.name}, " card: ", {p1card.value, p1card.suit})
    print({game.playerTwo.name}, " card: ", {p2card.value, p2card.suit})
    winner=Card.__gt__(Card, p1card, p2card)
    if winner==True:
        game.playerOne.add_card(p2card)
        game.playerOne.add_card(p1card)
        print({game.playerOne.name}, "wins the round!")
    else:
        game.playerTwo.add_card(p2card)
        game.playerTwo.add_card(p1card)
        print({game.playerTwo.name}, "wins the round!")

print(game.get_winner())


