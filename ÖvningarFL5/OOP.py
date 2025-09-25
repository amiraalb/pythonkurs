"""
Klasser och objekt
Skapa en klass Car med attributen brand och year.

Lägg till en metod description() som skriver ut “Märke: X, År: Y”.
Skapa två bil-objekt och skriv ut deras beskrivningar.
Utöka klassen Car med en metod age() som räknar ut hur gammal bilen är baserat på nuvarande år (tips: använd datetime).
"""
import datetime

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = int(year)

    def description(self):
        return f"Märke: {self.brand}, År: {self.year}"

    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

car1 = Car("Mercedes", "2002")
car2 = Car("Audi", "2021")

print(f"{car1.description()}, {car1.age()} år")
print(f"{car2.description()}, {car2.age()} år")