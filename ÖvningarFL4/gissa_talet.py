"""Gissa talet-spelet
Beskrivning: Skriv ett spel där datorn slumpmässigt väljer ett tal mellan 1 och 100. Användaren ska gissa talet.

Krav:

Använd try/except för att hantera om användaren inte skriver ett heltal.
Om gissningen är fel ska spelaren få veta om det hemliga talet är större eller mindre.
Programmet ska fortsätta tills spelaren gissar rätt.
"""


import random

def gissa_talet():
    computer_choice = random.randint(1, 100)

    while True:
        try:
            tal = int(input("Gissa ett tal mellan 1 och 100: "))
            if tal < 1 or tal > 100:
                print("Talet måste vara mellan 1 och 100.")
                continue

            if tal == computer_choice:
                print("Du har valt rätt tal!")
                break
            elif tal < computer_choice:
                print("För lågt, försök igen.")
            else:
                print("För högt, försök igen.")
        except ValueError:
            print("Du måste skriva ett heltal!")

gissa_talet()
