"Chips class for betting chips in blackjack game"

class Chips:
    " chips class with init total chips we have default chip are 100"
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
