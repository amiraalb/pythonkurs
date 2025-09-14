"""Skriv en funktion med namnet cut_edges.
Den ska ta en lista som parameter.
När den anropas ska den returnera en ny lista,
där den har tagit bort första och sista elementet. cut_edges([1, 2, 3, 4]) → [2, 3]`
"""

def cut_edges(min_lista):
    return min_lista[1:-1]

resultat = cut_edges([1, 2, 3, 4])
print(resultat) 
