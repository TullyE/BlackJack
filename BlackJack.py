'''
everything here is now a code along I tried doing it with the notebook walkthrough... It kinda worked?
but not completly
I was done with the project but wanted to complete it so I just watched the code along
'''
import random

#Vars
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        #GOT FROM NOTEBOOK
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE 
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:

        try:
            chips.bet = int(input('Place your bid: '))
        except:
            print('Whoops! That is an invalid bid')
        else:
            if chips.bet > chips.total: #GOT THE CHECK FROM THE NOTEBOOK ///I DON'T KNOW HOW TO PLAY BLACKJACK OKAY!\\\
                print("Sorry, you can't bid more than ", chips.total)
            else:
                print('Bid has been placed')
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace() #Didn't know to add this

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        player_option = input('Hit or Stand: ')
        if player_option == 'Hit':
            hit(deck, hand)
        elif player_option == 'Stand':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print('Whoops! Please type Hit or Stand')
            continue
        break

def show_some(player,dealer): #again copied from notebook
    print("\nDealer's Hand: ")
    print("<card hidden>")
    print(dealer.cards[1])  

    print("\n Players's hand:")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer): #copied from notebook
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's Hand is: {dealer.value}")

    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's Hand {player.value}")


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()
    
def push():
    return "Dealer and PLayer tie! It's a push!"

while True:
    # Print an opening statement
    print('Welcome to Blackjack! Made by Tully')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push()
        
        # Inform Player of their chips total 
        print(f'\nPlayer currently has {player_chips.total} chips')
        # Ask to play again (Copied from Notebook)
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break
'''
After redoing it with the walkthorugh I actuallyy did quite a bit of it correctly there was only small bits and pieces here and there where
I made some errors
Not too dissapointed with how this project went!

Would Have enjoyed it more ofc if I had known how to actually play Blackjack
I only vagly knew the rules... didn't know the ins/outs of it
'''