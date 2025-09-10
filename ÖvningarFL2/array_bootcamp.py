# Räkna ut summan i en lista
list = [1, -2, 3, -2, 4, -3]
result = sum(list)
print(f"Summan av siffrorna i listan är: {result}")

# Skapa en lista och skriv ut

filmer = ["Mission impossible", "The Shawshank Redemption", "Parasite", "Inception"]
print(filmer)

# Lägg till "Fellowship of the ring" sist i listan.

filmer.append("Fellowship of the ring")
print(filmer)

# Lägg till "The two towers" på första platsen i listan. (index noll)

filmer.insert(0, "The two towers")
print(filmer)

# Ta reda på vilken position (index) "Fellowship of the ring" har nu.
index = filmer.index("Fellowship of the ring")
print(index)

# Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
filmer.pop(0)
index = filmer.index("Fellowship of the ring")
print(index)

# Ta reda på hur lång listan är. (len)
len(filmer)
print(len(filmer))
print(filmer)

#Vänd listan baklänges.
filmer.reverse()
print(filmer)

# Sortera listan stigande i bokstavsordning.
filmer.sort()
print(filmer)