from Examination.player import Player, Dealer
from dice import Dice
from Examination.results import save_results


class Game:
    def __init__(self, target_score=21):
        self.target_score = target_score
        self.player = Player()
        self.dealer = Dealer()
        self.dice = Dice()

    def determine_winner(self, player_score, dealer_score):
        if player_score > self.target_score:
            return "dealer"
        elif dealer_score > self.target_score:
            return "player"
        elif player_score > dealer_score:
            return "player"
        elif dealer_score > player_score:
            return "dealer"
        else:
            return "draw"


def start_game():
    game = Game()
    print("Välkommen till spelet Blackjack med tärningar! \nDu spelar mot dealern. Målet är att komma så nära 21 poäng som möjligt utan att gå över.")

    while True:
        game.player.reset_score()
        game.dealer.reset_score()

        while True:
            print(f"\nNuvarande total poäng: {game.player.score}")
            try:
                choice = int(input("1. Rulla tärningen (värde 1-6) \n2. Stanna \n"))
                if choice == 1:
                    roll = game.dice.roll()
                    print(f"Tärningen visar: {roll}")
                    game.player.score += roll
                    if game.player.score > game.target_score:
                        print("Du gick över 21! Du förlorade.")
                        game.player.fails += 1
                        break
                elif choice == 2:
                    print("\nDealerns tur att rulla.")
                    while game.dealer.score < 17:
                        roll = game.dice.roll()
                        game.dealer.score += roll
                        print(f"Tärningen visar: {roll} (Total: {game.dealer.score})")

                    winner = game.determine_winner(game.player.score, game.dealer.score)
                    if winner == "player":
                        print("Du vinner!")
                        game.player.wins += 1
                    elif winner == "dealer":
                            print("Dealern vinner!")
                            game.player.fails += 1
                    else:
                        print("Det blev oavgjort!")
                        game.player.draw += 1
                    break
                else:
                    print("Ange ett giltigt alternativ (1 eller 2).")
            except ValueError:
                print("Du måste skriva ett heltal!")

        print(f"\nDina vinster: {game.player.wins}, Dealerns vinster: {game.player.fails}, Oavgjort: {game.player.draw}")

        while True:
            again = input("\nVill du spela en gång till? (ja/nej): ").lower()
            if again == 'ja':
                break
            elif again == 'nej':
                print("Tack för att du spelade!")
                save_results(game.player)
                return
            else:
                print("Ange ett giltigt svar: 'ja' eller 'nej'.")

if __name__ == "__main__":
    start_game()
