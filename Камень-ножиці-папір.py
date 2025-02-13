import random

options = ["камінь", "ножиці", "папір"]

user_choice = input("Оберіть (камінь, ножиці, папір): ").lower()
computer_choice = random.choice(options)

print(f"Комп'ютер обрав: {computer_choice}")

if user_choice == computer_choice:
    print("Нічия!")
elif (user_choice == "камінь" and computer_choice == "ножиці") or \
     (user_choice == "ножиці" and computer_choice == "папір") or \
     (user_choice == "папір" and computer_choice == "камінь"):
    print("Ви перемогли!")
else:
    print("Ви програли!")
