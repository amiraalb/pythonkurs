class Player:
    def __init__(self):
        self.score = 0
        self.fails = 0
        self.wins = 0
        self.draw = 0

    def reset_score(self):
        self.score = 0


class Dealer(Player):
    pass
