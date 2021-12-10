# Write your blackjack game here.
import random

SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]
SCORES = {2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

class Card:
    def __init__(self, suit, rank, score):
        self.suit = suit
        self.rank = rank
        self.score = score
        

    def __str__(self):
        return f'{self.rank} of {self.suit} {self.score}'

class Deck:
    def __init__(self, suits, scores):
        self.cards = []
   
        for suit in suits:
            for value in scores.keys():
                card = Card(suit, value, scores.get(value))
                self.cards.append(card)
    
    def show_cards(self): 
        for card in self.cards:
            print(card)

    def draw_card(self):               
        drawn_card = random.choice(self.cards)
        self.cards.remove(drawn_card)
        return drawn_card
   
class Player:
    def __init__(self):
        self.hand = []
    
    def __str__(self):
        return "Player"

    def show_hand(self):
        print("Player")
        for card in self.hand:
            print(card)

class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return "Dealer"

    def show_hand(self):
        print("Dealer")
        for card in self.hand:
            print(card)

class Game:
    def __init__(self, suits, scores):
        self.player = Player()
        self.dealer = Dealer()
        self.gamedeck = Deck(suits, scores)

    def deal_cards(self):
        for i in range(2):
            self.dealer.hand.append(self.gamedeck.draw_card())
            self.player.hand.append(self.gamedeck.draw_card())
        self.dealer.show_hand()
        self.player.show_hand()


         

            





game = Game(SUITS, SCORES)
game.deal_cards()
# gamedeck.show_cards()


# for i in range(2):
#     deal_card(deck, dealer)
#     deal_card(deck, player)

# dealer.show_hand()
# player.show_hand()
# print(len(deck))



    #starts game by calling GameRound
    #keeps tabs of scores
    #game can end if player busts, or if dealer busts or hits 18
    #declares winner




            

# class Dealer:
#     def __init__(self):
#         self.name = 

# class Game:
#     def __init__(self):
#         self.endGame = False
#         #self.player = Player("Player")
#         #self.dealer = Player("Dealer")
#     def start(self):
#         while not self.endGame:
#             #GameRound(self.player, self.dealer)






