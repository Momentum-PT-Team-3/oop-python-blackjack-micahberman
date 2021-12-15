# Write your blackjack game here.
import random

SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]
SCORES = {2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.calculate_value(self.rank)
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def calculate_value(self, rank):
        values_dictionary = {
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            "J":10,
            "Q":10,
            "K":10,
            "A":11
        }
        card_value = values_dictionary[rank]
        return card_value

    


class Deck:
    def __init__(self, suits, scores):
        self.cards = []
   
        for suit in suits:
            for value in scores.keys():
                card = Card(suit, value)
                self.cards.append(card)
                # cardscore = card.score
                # print (cardscore)

    def show_cards(self): 
        for card in self.cards:
            print(card)

    def draw_card(self):               
        drawn_card = random.choice(self.cards)
        self.cards.remove(drawn_card)
        return drawn_card

    def get_score(self):
        card_score = Card.get_score()
        return card_score

   
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
        self.player_score = 0
        self.dealer_score = 0

    def deal_cards(self):
        for i in range(2):
            self.dealer.hand.append(self.gamedeck.draw_card())
            self.player.hand.append(self.gamedeck.draw_card())
        self.dealer.show_hand()
        self.player.show_hand()


    def hit(self, person):
        person.hand.append(self.gamedeck.draw_card())
        person.show_hand()

    def calculate_totals(self, dealer):
        self.dealer_hand_values = []
        for card in dealer.hand:
            self.dealer_hand_values.append(card.value)
        self.dealer_score = sum(self.dealer_hand_values)
    
    def deal_dealer(self):
        while self.dealer_score < 17:
            self.hit(self.dealer)
            self.calculate_totals(self.dealer)
            print(self.dealer_score)
        else:
            print('Hit 17, stopping.')
            print(self.dealer_score)

    def hit_or_stay(self):
        choice = input("Would you like to hit? y/n")
        while choice == 'y':
            self.hit(self.player)
            choice = input('Would you like to hit again? y/n')
        else:
            self.player.show_hand()



game = Game(SUITS, SCORES)
game.deal_cards()
# game.hit_or_stay()
game.deal_dealer()










