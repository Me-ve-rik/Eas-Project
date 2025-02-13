import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Вгадайте число (1-100): "))
    if guess < number:
        print("Занадто мале!")
    elif guess > number:
        print("Занадто велике!")
    else:
        print("Вітаю! Ви вгадали!")