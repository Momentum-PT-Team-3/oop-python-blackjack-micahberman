# Write your blackjack game here.
# import random

# suits =["Hearts", "Spades", "Clubs", "Diamonds"]
# numbers = range(1,14)
# deck = []


# while len(deck) != 312:
#     for suit in suits:
#         for number in numbers:
#             deck.append(f'{number} of {suit}')

#     print(f'There are {len(deck)} cards in the deck.')

# play_hand = []
# deal_hand_shown = []
# deal_hand_hidden = []

# while len(deal_hand_hidden) != 1:
#     player_card_1 = random.choice(deck)
#     deck.remove(player_card_1)
#     play_hand.append(player_card_1)
#     dealer_card_shown = random.choice(deck)
#     deck.remove(dealer_card_shown)
#     deal_hand_shown.append(dealer_card_shown)
#     player_card_2 = random.choice(deck)
#     deck.remove(player_card_2)
#     play_hand.append(player_card_2)
#     dealer_card_hidden = random.choice(deck)
#     deck.remove(dealer_card_hidden)
#     deal_hand_hidden.append(dealer_card_hidden)

    
# print(f'There are {len(deck)} cards left in the deck.')
# print('The player has the following cards in their hand:')
# print(play_hand)
# print('You can see the dealer has a:')
# print(deal_hand_shown)
# print('You cannot see that the dealer has a:')
# print(deal_hand_hidden)

# choice = input('Would you like to hit? Y/N')
# while choice == 'Y' or 'y':
#     new_card = random.choice(deck)
#     deck.remove(new_card)
#     play_hand.append(new_card)
#     print(f'Your new card is a {number} of {suit}')
#     choice = input('Would you like to hit again?')
# if choice == 'N' or 'n':
#     deck_value = sum()

#START OOP VERSION OF BLACKJACK

#TODO: Make GameRound class - methods call Deck function to give it cards, 
        # manage how many cards each PC player has, tabulates scores based on card values
       #tells who's turn it is
#TODO: Make Deck class - methods create deck, card values, and distributes cards to GameRound
#TODO: Make Dealer class - calls Deck function to give it cards, manages how many cards the dealer has, tabluates score based on card values
#TODO: Make Game class - methods calls GameRound and compares Dealer score and Player score
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
        
        

def deal_card(deck):               
    drawn_card = random.choice(deck)
    print(drawn_card)

    deck.remove(drawn_card)

    

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

    def deal_card(deck, card_player):               
        drawn_card = random.choice(deck)
        deck.remove(drawn_card)
        card_player.hand.append(drawn_card)





gamedeck = Deck(SUITS, SCORES)
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






