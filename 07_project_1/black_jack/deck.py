"Deck class are list of card used to play blackjack games"
import random
import card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
#          'Queen':10, 'King':10, 'Ace':11}
class Deck:
    " Deck class are populate card class becoming one Deck card"
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(card.Card(suit,rank))
                # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for single_card in self.deck:
            deck_comp += '\n '+single_card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        "Shuffle list of self.decl"
        random.shuffle(self.deck)

    def deal(self):
        "Dealing one card to player hands from deck"
        single_card = self.deck.pop()
        return single_card
    