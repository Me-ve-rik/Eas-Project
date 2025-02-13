# Функція для перевірки паролю
def validate_password(password):
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
        return True
    return False

# Початок анкети
print("Ласкаво просимо до анкети!")

name = input("Як вас звати? ")
age = input("Скільки вам років? ")
hobby = input("Які ваші хобі? ")

# Перевірка паролю
while True:
    password = input("Створіть пароль (мінімум 8 символів, літери та цифри): ")
    if validate_password(password):
        print("Пароль успішно створено!")
        break
    else:
        print("Пароль недостатньо сильний. Спробуйте ще раз.")

# Виведення результатів анкети
print("\nДякуємо за заповнення анкети!")
print(f"Привіт, {name}! Вам {age} років, і ви любите {hobby}.")
print("Не забудьте свій пароль!")