#def vinterjacka(pris):
#    rea_pris = pris * 0.5
#    print(f"Vinterjackan kostar: {rea_pris} efter rabatt.")

#vinterjacka(2000)

def vinterjacka():
    procent = float(input("Skriv in en procentsats (t.ex. 10 för 10%).\n"))
    rabatt = 2000 * (procent / 100)
    rea_pris = 2000 - rabatt
    print(f"Vinterjackan kostar: {rea_pris} efter rabatt.")

vinterjacka()
