def biggest():
    a = int(input("Skriv in ett numeriskt värde.\n"))
    b = int(input("Skriv in ett till numeriskt värde.\n"))

    if a > b:
        print(f"{a} är större än {b}")
    else:
        print(f"{b} är större än {a}")

biggest()
