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

    def reset_score(self):
        self.score = 0

class Dealer(Player):
    pass

class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def determine_winner(player_score, dealer_score, target=21):
    if player_score > target:
        return "dealer"
    elif dealer_score > target:
        return "player"
    elif player_score > dealer_score:
        return "player"
    elif dealer_score > player_score:
        return "dealer"
    else:
        return "draw"

def save_results(player):
    with open('resultat.txt', 'w') as file:
        file.write(f"Vinster: {player.wins}\n")
        file.write(f"Förluster: {player.fails}\n")
        file.write(f"Oavgjorda: {player.draw}\n")
    print("Resultat har sparats i resultat.txt")

def start_game():
    game = Game()
    player = Player()
    dealer = Dealer()
    dice = Dice()

    print("Välkommen till spelet Blackjack med tärningar! \nDu spelar mot dealern. Målet är att komma så nära 21 poäng som möjligt utan att gå över.")

    while True:
        player.reset_score()
        dealer.reset_score()

        while True:
            print(f"\nNuvarande total poäng: {player.score}")
            try:
                choice = int(input("1. Rulla tärningen (värde 1-6) \n2. Stanna \n"))
                if choice == 1:
                    roll = dice.roll()
                    print(f"Tärningen visar: {roll}")
                    player.score += roll
                    if player.score > game.target_score:
                        print("Du gick över 21! Du förlorade.")
                        player.fails += 1
                        break
                elif choice == 2:
                    print("\nDealerns tur att rulla.")
                    while dealer.score < 17:
                        roll = dice.roll()
                        dealer.score += roll
                        print(f"Tärningen visar: {roll} (Total: {dealer.score})")

                    winner = determine_winner(player.score, dealer.score, game.target_score)
                    if winner == "player":
                        print("Du vinner!")
                        player.wins += 1
                    elif winner == "dealer":
                        if dealer.score > game.target_score:
                            print("Dealern gick över 21! Du vinner!")
                            player.wins += 1
                        else:
                            print("Dealern vinner!")
                            player.fails += 1
                    else:
                        print("Det blev oavgjort!")
                        player.draw += 1
                    break
                else:
                    print("Ange ett giltigt alternativ (1 eller 2).")
            except ValueError:
                print("Du måste skriva ett heltal!")

        print(f"\nDina vinster: {player.wins}, Dealerns vinster: {player.fails}, Oavgjort: {player.draw}")

        again = input("\nVill du spela en gång till? (ja/nej): ").lower()
        if again != 'ja':
            print("Tack för att du spelade!")
            save_results(player)
            break

if __name__ == "__main__":
    start_game()
