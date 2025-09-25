"""Skapa en basklass Vehicle med attribut brand och en metod drive().

Skapa två underklasser Car och Bicycle som överskuggar metoden drive() med olika utskrifter.
Lägg objekten i en lista och loopa över dem.
Lägg till en ny klass Boat och se om programmet fungerar utan ändringar."""

class Vehicle():
    def __init__(self, brand):
        self.brand = brand

def drive(self):
    return f"Märke: {self.brand}"
class Car(Vehicle):
    brand = "Audi"
    print(brand)

class Bicycle(Vehicle):
    brand = "MountainBike"
    print(brand)

#Ej klar