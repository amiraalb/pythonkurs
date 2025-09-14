"""
Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:

pretty_print(["a", "b", 3.14])
Listan har 3 element:
1. a
2. b
3. 3.14

"""

def pretty_print(min_lista):
    if not min_lista:
        print("Listan är tom.")
    else:
        print(f"Listan har {len(min_lista)} element:")
        for i in range(len(min_lista)):
            print(f"{i + 1}. {min_lista[i]}")

pretty_print(["a", "b", 3.14])
