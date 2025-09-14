"""
Skriv en funktion som tar tre parametrar.
De första två är två tal och den sista är en operator d.v.s antingen '+', '-', '/', '*'.
Utför beräkningen och returnera summan och skriv ut.
Det ska enbart gå att skicka med siffror (förutom operanden som är en sträng då)
och varje operation ska vara sin egen funktion.
"""

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

def calculate(num1, num2, operator):

    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)

resultat = calculate(1, 5, "-")
print(resultat)
