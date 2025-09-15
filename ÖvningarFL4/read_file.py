"""
Enkel filbaserad miniräknare
Beskrivning: Skapa en miniräknare som läser in en lista med uträkningar från en textfil och räknar ut resultaten.

Krav:

Varje rad i filen innehåller en uträkning, t.ex. 10 / 2, 5 + 3.
Programmet ska hantera:
FileNotFoundError om filen inte finns.
ZeroDivisionError om division med noll sker.
ValueError eller syntaxfel i inmatade uttryck.
Resultaten ska sparas i en ny fil resultat.txt.
"""


import calculator

def read_file():
    try:
        with open('data.txt') as file:
            file_content = file.readlines()

		with open('resultat.txt', 'w') as resultat_fil:
        	radnummer = 1
        	for rad in file_content:
            	tal = rad.strip()

            	if tal == "":
                	radnummer += 1
                	continue

            	delar = tal.split()

            tal1_str, operator, tal2_str = delar

            try:
                tal1 = float(tal1_str)
                tal2 = float(tal2_str)
                resultat = calculator.calculate(tal1, tal2, operator)
                resultat_fil.write(f"Rad {radnummer}: {tal} = {resultat}")
            except ZeroDivisionError:
                resultat_fil.write(f"Rad {radnummer}: Det går inte att dela med 0!")
            except ValueError:
                resultat_fil.write(f"Rad {radnummer}: Ogiltiga tal.")

            radnummer += 1
		print("Resultaten har sparats i resultat.txt")

    except FileNotFoundError:
        print("Filen hittades inte.")

read_file()
