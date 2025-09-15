def add(tal1, tal2):
    return tal1 + tal2

def subtract(tal1, tal2):
    return tal1 - tal2

def divide(tal1, tal2):
    return tal1 / tal2

def multiply(tal1, tal2):
    return tal1 * tal2

def calculate(tal1, tal2, operator):

    if operator == '+':
        return add(tal1, tal2)
    elif operator == '-':
        return subtract(tal1, tal2)
    elif operator == '/':
        return divide(tal1, tal2)
    elif operator == '*':
        return multiply(tal1, tal2)
