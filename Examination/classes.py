import random

class Game():
    def __init__(self):
            self.target_score = 21
class Player:
    def __init__(self):
            self.score = 0
            self.fails = 0
            self.wins = 0
            self.draw = 0
class Dealer(Player):
   pass
class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)
class Highscore():
    def __init__(self):
        self.highscore = 0

    def show_highscore(self):
        print(f"Highscore: {self.highscore}")

