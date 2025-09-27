def save_results(player):
    with open('resultat.txt', 'w') as file:
        file.write(f"Dina vinster: {player.wins}\n")
        file.write(f"Dina förluster: {player.fails}\n")
        file.write(f"Oavgjorda: {player.draw}\n")
    print("Resultatet har sparats i resultat.txt")