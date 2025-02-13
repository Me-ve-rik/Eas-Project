num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Оберіть операцію (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Ділення на нуль неможливе")
else:
    print("Невірна операція")