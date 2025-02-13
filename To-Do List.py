tasks = []

while True:
    print("\n1. Додати завдання\n2. Переглянути завдання\n3. Видалити завдання\n4. Вийти")
    choice = input("Оберіть дію: ")

    if choice == "1":
        task = input("Введіть завдання: ")
        tasks.append(task)
        print("Завдання додано.")
    elif choice == "2":
        print("Список завдань:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        index = int(input("Введіть номер завдання для видалення: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Завдання '{removed}' видалено.")
        else:
            print("Неправильний номер.")
    elif choice == "4":
        break
    else:
        print("Невірний вибір.")