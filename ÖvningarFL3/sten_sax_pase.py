"""

Lägg även till så att man kan spela igen och antalet vinster / förluster hålls reda på.

Experimentera med att dela upp koden i moduler.
"""
import random
def sten_sax_pase():
    min_lista = ["Sten", "Sax", "Påse"]

    val = input("Skriv in sten, sax, eller påse:\n").capitalize()
    print(f"Du har valt: {val}.")

    computer_choice = random.choice(min_lista)
    print(f"Datorn väljer: {computer_choice}.")

    if val == computer_choice:
        print("Du och datorn har valt samma! Det är oavgjort.")
    elif val == "Sten" and computer_choice == "Sax":
        print("Du vann!")
    elif val == "Sten" and computer_choice == "Påse":
        print("Datorn vann!")
    elif val == "Sax" and computer_choice == "Sten":
        print("Datorn vann!")
    elif val == "Sax" and computer_choice == "Påse":
        print("Du vann!")
    elif val == "Påse" and computer_choice == "Sten":
        print("Du vann!")
    elif val == "Påse" and computer_choice == "Sax":
        print("Datorn vann!")
    else:
        print("Ogiltigt val.")




sten_sax_pase()