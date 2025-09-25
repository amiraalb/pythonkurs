import classes

def start_game():
    game = Game()
    player = Player()
    dealer = Dealer()
    dice = Dice()

    print("Välkommen till spelet Blackjack med tärningar! \nDu spelar mot dealern och den som kommer närmast 21 utan att gå över vinner!")

    while True:
        player.reset_score()
        dealer.reset_score()

        while True:
            print(f"\nDin poäng: {player.score}")
            try:
                choice = int(input("Gör ett val: \n1. Rulla tärningen \n2. Stanna \n"))
                if choice == 1:
                    roll = dice.roll()
                    print(f"Du rullade: {roll}")
                    player.score += roll
                    if player.score > game.target_score:
                        print("Du gick över 21! Du förlorade.")
                        player.fails += 1
                        break
                elif choice == 2:
                    print("\nDealern börjar rulla...")
                    while dealer.score < 17:
                        roll = dice.roll()
                        dealer.score += roll
                        print(f"Dealern rullade: {roll} (Total: {dealer.score})")

                    if dealer.score > game.target_score:
                        print("Dealern gick över 21! Du vinner!")
                        player.wins += 1
                    elif dealer.score > player.score:
                        print("Dealern vinner!")
                        player.fails += 1
                    elif dealer.score < player.score:
                        print("Du vinner!")
                        player.wins += 1
                    else:
                        print("Det blev oavgjort!")
                        player.draw += 1
                    break
                else:
                    print("Ange ett giltigt alternativ (1 eller 2).")
            except ValueError:
                print("Du måste skriva ett heltal!")

        print(f"\nStatistik: Vinster: {player.wins}, Förluster: {player.fails}, Oavgjort: {player.draw}")

        again = input("\nVill du spela en gång till? (ja/nej): ").strip().lower()
        if again != 'ja':
            print("Tack för att du spelade!")
            break

start_game()