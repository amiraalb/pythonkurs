def får_åka_balder():
    åkband = input("Vilket åkband har du; small, medium, large eller platinum?:\n")

    if åkband == "small" or åkband == "medium":
        print("Du får inte åka Balder!")
    elif åkband == "large" or åkband == "platinum":
        print("Du får åka Balder!")
    else:
        print("Ogiltigt åkband.")

får_åka_balder()