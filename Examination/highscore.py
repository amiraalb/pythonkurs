def save_highscore(player):
    with open('resultat.txt', 'w') as file:
        file.write(f"Dina vinster: {player.wins}\n")
        file.write(f"Dealerns vinster: {player.fails}\n")
        file.write(f"Oavgjort: {player.draw}\n")
    print("Resultatet har sparats i resultat.txt")