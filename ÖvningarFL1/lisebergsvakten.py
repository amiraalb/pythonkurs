def får_åka_helix(längd_cm):
    return längd_cm >= 150

längd = int(input("Ange din längd i cm: "))
får_åka = får_åka_helix(längd)
print(får_åka)
