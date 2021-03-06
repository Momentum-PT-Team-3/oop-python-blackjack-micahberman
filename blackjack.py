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

class GameRound:
    def __init__(self, suits, scores):
        self.player = Player()
        self.dealer = Dealer()
        self.gamedeck = Deck(suits, scores)
        self.player_score = 0
        self.dealer_score = 0
        self.winner_player = False
        self.winner_dealer = False

    def replay_game(self):
        game = GameRound(SUITS, SCORES)
        game.deal_cards()
        game.deal_dealer()
        game.hit_or_stay()


    def deal_cards(self):
        for i in range(2):
            self.dealer.hand.append(self.gamedeck.draw_card())
            self.player.hand.append(self.gamedeck.draw_card())
        self.dealer.show_hand()
        self.player.show_hand()


    def hit(self, person):
        person.hand.append(self.gamedeck.draw_card())
        person.show_hand()

    def calculate_totals(self, dealer, player):
        dealer_hand_values = []
        player_hand_values = []
        for card in dealer.hand:
            dealer_hand_values.append(card.value)
        self.dealer_score = sum(dealer_hand_values)
        for card in player.hand:
            player_hand_values.append(card.value)
        self.player_score = sum(player_hand_values)
    
    def deal_dealer(self):
        while self.dealer_score < 17:
            self.hit(self.dealer)
            self.calculate_totals(self.dealer, self.player)
            if self.dealer_score > 21:
                print('The dealer busts! Player wins.')
                self.winner_player = True
                replay_choice = input('Would you like to play again? y/n')
                if replay_choice == 'y':
                    self.replay_game()
                else:
                    print('Thanks for playing!')
                    break
            if self.dealer_score == 21:
                print('The dealer gets blackjack! You lose.')
                dbj_replay_choice = input('Would you like to play again? y/n')
                if dbj_replay_choice == 'y':
                    self.replay_game()
                else:
                    print('Thanks for playing!')
                    exit()
        else:
            print(f'The dealer stays with a {self.dealer_score}.')

            

    def hit_or_stay(self):
        print(f'Your score is currently {self.player_score}')
        while self.player_score < 21:
            choice = input('Would you like to hit? y/n')
            if choice == 'n':
                print(f'Your score is now {self.player_score}')
                if self.player_score > self.dealer_score:
                    print(f'Your score of {self.player_score} is higher than the dealer\'s score of {self.dealer_score}. You win!')
                    pws_replay_choice = input('Would you like to play again? y/n')
                    if pws_replay_choice == 'y':
                        self.replay_game()
                    else:
                        print('Thanks for playing!')
                        exit()
                else:
                    print(f'Your score of {self.player_score} is lower than the dealer\'s score of {self.dealer_score}. You lose.')
                    pds_replay_choice = input('Would you like to play again? y/n')
                    if pds_replay_choice == 'y':
                        self.replay_game()
                    else:
                        print('Thanks for playing!')
                        exit()

            self.hit(self.player)
            self.calculate_totals(self.dealer, self.player)
            print(f'Your score is now {self.player_score}')
        else:
            if self.player_score == 21:
                print('You got Blackjack! Here\'s a million dollars.')
                pw_replay_choice = input('Would you like to play again? y/n')
                if pw_replay_choice == 'y':
                    self.replay_game()
                else: 
                    print('Thanks for playing!')
                    exit()
            else:
                print(f'Your score is now {self.player_score}. You busted!')
                pb_replay_choice = input('Would you like to play again? y/n')
                if pb_replay_choice == 'y':
                    self.replay_game()
                else:
                    print('Thanks for playing!')
                    exit()


        
                

game = GameRound(SUITS, SCORES)
game.deal_cards()
game.deal_dealer()
game.hit_or_stay()










