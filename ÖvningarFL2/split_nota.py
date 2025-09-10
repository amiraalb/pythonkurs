# Version 1:
"""""
nota = []
answer = ""

while answer != "avsluta":
    answer = input("Välkommen till Split the nota! Avsluta genom att skriva: avsluta \nSkriv in ett belopp: ")

    if answer != "avsluta":
        nota.append(int(answer))
        print(nota)
    elif answer == "avsluta":
        result = sum(nota)
        print(f"Det blir {result} kr totalt. Välkommen åter!")
"""
# Version 2:

"""Version 2: programmet ska fråga hur många man är, 
och tala om hur mycket varje person i sällskapet ska betala. 
Hur många är ni? 3 
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!"""

nota = []

print("Välkommen till Split the nota! Avsluta genom att skriva: avsluta")

antal_personer = input("Hur många är ni?: ")

if antal_personer != "avsluta":
    antal_personer = int(antal_personer)

    for i in range(antal_personer):
        belopp = float(input(f"Skriv in ett belopp för person {i + 1}: "))
        nota.append(belopp)

    total = sum(nota)
    per_person = total / antal_personer

    print(f"Det blir {total} kr totalt, alltså {per_person} kr per person. Välkommen åter!")
