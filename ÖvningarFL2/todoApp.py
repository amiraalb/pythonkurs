todos = []
answer = ""

while answer != "klar":
    answer = input("Vad är din todo?\nSkriv 'visa' för att visa alla todos.\nSkriv 'remove' för att ta bort en todo.\nSkriv 'redigera' för att redigera en todo.\nSkriv 'klar' för att avsluta\n")

    if answer != "klar" and answer != "visa" and answer != "remove" and answer != "redigera":
        todos.append(answer)
        print("Todo tillagd")
    elif answer == "visa":
        print("-----Todos-----")
        for i in range(len(todos)):
            print(f"{i + 1}. {todos[i]}")
    elif answer == "remove":
        index = int(input("Vilken todo vill du ta bort? Ange index. "))
        if 0 <= index < len(todos):
            removed_todo = todos.pop(index)
            print(f"'{removed_todo}' har tagits bort.")
    elif answer == "redigera":
        i = int(input("Vilken todo vill du redigera? Ange index. "))
        for i in range(len(todos)):
            ny_todo = input("Ange ny todo: ")
            todos[i] = ny_todo
            print(f"'{ny_todo}' har lagts till.")
